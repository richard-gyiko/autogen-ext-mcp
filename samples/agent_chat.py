import asyncio
from typing import List

from autogen_core import CancellationToken
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import HandoffTermination, TextMentionTermination
from autogen_agentchat.messages import HandoffMessage
from autogen_agentchat.teams import BaseGroupChat, RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from mcp import ClientSession, StdioServerParameters, stdio_client
from rich.console import Console as RichConsole
from autogen_ext_mcp.tools import get_tools_from_mcp_server, MCPToolAdapter

mcp_servers = [
    StdioServerParameters(
        command="npx.cmd",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "C:\\Users\\gyiko\\Desktop",
        ],
    ),
]


def print_tools(tools: List[MCPToolAdapter]) -> None:
    console = RichConsole()
    console.print("\n[bold blue]Loaded MCP Tools:[/bold blue]")

    for tool in tools:
        console.print(tool.schema, style="dim")
        console.print()


async def load_tools():
    tools_list = [await get_tools_from_mcp_server(server) for server in mcp_servers]

    # Flatten the list of tools
    tools = [tool for sublist in tools_list if sublist for tool in sublist]

    for tool in tools:
        print("--- TOOL SCHEMA COMPARISON ---")
        print("Generated Tool Schema:")
        print(tool.schema)
        print("Original Tool Schema:")
        print(tool._tool.inputSchema)
        print("--- END TOOL SCHEMA COMPARISON ---")

    return tools


async def run_team_stream(team: BaseGroupChat, initial_task: str) -> None:
    task_result = await Console(team.run_stream(task=initial_task))
    last_message = task_result.messages[-1]

    while isinstance(last_message, HandoffMessage) and last_message.target == "user":
        user_message = input("User: ")

        if user_message == "exit":
            break

        task_result = await Console(
            team.run_stream(
                task=HandoffMessage(
                    source="user", target=last_message.source, content=user_message
                )
            )
        )
        last_message = task_result.messages[-1]


async def main():
    tools = await load_tools()

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0)

    agent = AssistantAgent(
        name="mcp_tools_agent",
        model_client=model_client,
        tools=tools,
        handoffs=["user"],
        system_message="""
You are a helpful AI assistant!
When the user task is complete, type 'TERMINATE' to end the conversation.
If you need clarification, handoff to the user.
""",
    )

    team = RoundRobinGroupChat(
        participants=[agent],
        termination_condition=TextMentionTermination("TERMINATE")
        | HandoffTermination(target="user"),
    )

    user_input = input("> ")

    if user_input != "exit":
        await run_team_stream(team, user_input)


async def test():
    async with stdio_client(mcp_servers[0]) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "list_directory", {"path": "c:\\users\\gyiko\\desktop"}
            )

            print(result)

            tools = await session.list_tools()
            # Get the tool called "list_directory"
            list_directory_tool = next(
                (tool for tool in tools.tools if tool.name == "list_directory"), None
            )

            print(list_directory_tool)

            tool_adapter = MCPToolAdapter(mcp_servers[0], tool=list_directory_tool)

            # Create a proper Pydantic model instance using the tool's args_type
            input_data = {"path": "c:\\users\\gyiko\\desktop"}
            args = tool_adapter.args_type().model_validate(input_data)

            result = await tool_adapter.run(
                args, cancellation_token=CancellationToken()
            )
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
