from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.sse import sse_client

from .adapter import StdioMCPToolAdapter, SseMCPToolAdapter, SseServerParameters


async def get_tools_from_stdio_mcp_server(server_params: StdioServerParameters):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_list = await session.list_tools()

            return [
                StdioMCPToolAdapter(server_params, tool) for tool in tools_list.tools
            ]


async def get_tools_from_sse_mcp_server(server_params: SseServerParameters):
    async with sse_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_list = await session.list_tools()

            return [SseMCPToolAdapter(server_params, tool) for tool in tools_list.tools]
