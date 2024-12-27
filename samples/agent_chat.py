import asyncio
from pathlib import Path
from typing import List

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext_mcp.tools import get_tools_from_mcp_server, MCPToolAdapter
from mcp import StdioServerParameters
from dotenv import load_dotenv
from rich.console import Console as RichConsole

# Get desktop path cross-platform
desktop_path = str(Path.home() / "Desktop")

mcp_server = StdioServerParameters(
    command="npx.cmd",
    args=[
        "-y",
        "@modelcontextprotocol/server-filesystem",
        desktop_path,
    ],
)


def print_tools(tools: List[MCPToolAdapter]) -> None:
    console = RichConsole()
    console.print("\n[bold blue]📦 Loaded MCP Tools:[/bold blue]")

    for tool in tools:
        console.print(f"\n[bold green]🔧 {tool.schema['name']}[/bold green]")
        if 'description' in tool.schema:
            console.print(f"[italic]{tool.schema['description']}[/italic]")
        
        if 'parameters' in tool.schema:
            console.print("\n[yellow]Parameters:[/yellow]")
            params = tool.schema['parameters']
            if 'properties' in params:
                for prop_name, prop_details in params['properties'].items():
                    required = prop_name in params.get('required', [])
                    required_mark = "[red]*[/red]" if required else ""
                    console.print(f"  • [cyan]{prop_name}{required_mark}[/cyan]: {prop_details.get('type', 'any')}")
                    if 'description' in prop_details:
                        console.print(f"    [dim]{prop_details['description']}[/dim]")
        
        console.print("─" * 50)


async def main():
    tools = await get_tools_from_mcp_server(mcp_server)
    print_tools(tools)

    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0)

    agent = AssistantAgent(
        name="mcp_tools_agent",
        model_client=model_client,
        tools=tools,
    )

    user_input = "Create a file called 'autogen.md' on my desktop with the following content: 'Hello, World!'"

    await Console(
        agent.run_stream(task=user_input, cancellation_token=CancellationToken())
    )


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
