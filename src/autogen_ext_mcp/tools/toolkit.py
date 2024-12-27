from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from .adapter import MCPToolAdapter


async def get_tools_from_mcp_server(server_params: StdioServerParameters):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_list = await session.list_tools()

            return [MCPToolAdapter(server_params, tool) for tool in tools_list.tools]
