import asyncio
from pathlib import Path
from typing import List

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from rich.console import Console as RichConsole

from autogen_ext_mcp.tools import (
    StdioMcpToolAdapter,
    StdioServerParams,
    mcp_server_tools,
)


file_system_mcp_server = StdioServerParams(
    command="npx.cmd",
    args=[
        "-y",
        "@modelcontextprotocol/server-filesystem",
        str(Path.home() / "Desktop"),
    ],
)

fetch_mcp_server = StdioServerParams(
    command="uvx",
    args=[
        "mcp-server-fetch",
    ],
)


def print_tools(tools: List[StdioMcpToolAdapter]) -> None:
    """Print available MCP tools and their parameters in a formatted way."""
    console = RichConsole()
    console.print("\n[bold blue]📦 Loaded MCP Tools:[/bold blue]\n")

    for tool in tools:
        # Tool name and description
        console.print(f"[bold green]🔧 {tool.schema.get('name', 'Unnamed Tool')}[/bold green]")
        if description := tool.schema.get('description'):
            console.print(f"[italic]{description}[/italic]\n")

        # Parameters section
        if params := tool.schema.get('parameters'):
            console.print("[yellow]Parameters:[/yellow]")
            if properties := params.get('properties', {}):
                required_params = params.get('required', [])
                for prop_name, prop_details in properties.items():
                    required_mark = "[red]*[/red]" if prop_name in required_params else ""
                    param_type = prop_details.get('type', 'any')
                    console.print(f"  • [cyan]{prop_name}{required_mark}[/cyan]: {param_type}")
                    if param_desc := prop_details.get('description'):
                        console.print(f"    [dim]{param_desc}[/dim]")

        console.print("─" * 60 + "\n")


async def main():
    file_system_tools = await mcp_server_tools(file_system_mcp_server)
    fetch_tools = await mcp_server_tools(fetch_mcp_server)

    print_tools(file_system_tools)
    print_tools(fetch_tools)

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0)

    agent = AssistantAgent(
        name="mcp_tools_agent",
        model_client=model_client,
        tools=fetch_tools + file_system_tools,
        system_message="You are a helpful AI assistant. Respond with 'TERMINATE' when fulfilled the user task.",
    )

    team = RoundRobinGroupChat(
        participants=[agent],
        max_turns=10,
        termination_condition=TextMentionTermination("TERMINATE"),
    )

    user_input = "Fetch the docs on https://modelcontextprotocol.io/development/updates and extract its contents as markdown then create a file called 'autogen.md' on my desktop with the fetched content."

    await Console(
        team.run_stream(task=user_input, cancellation_token=CancellationToken())
    )


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
