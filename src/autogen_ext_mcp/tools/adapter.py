from typing import Any, Type

from autogen_core import CancellationToken, Component, ComponentBase
from autogen_core.tools import BaseTool
from json_schema_to_pydantic import create_model
from mcp import ClientSession, StdioServerParameters, Tool, stdio_client
from pydantic import BaseModel


class MCPToolAdapterConfig(BaseModel):
    """Configuration for the MCP tool adapter."""

    server_params: StdioServerParameters
    tool: Tool


class MCPToolAdapter(
    BaseTool[BaseModel, Any],
    ComponentBase[MCPToolAdapterConfig],
    Component[MCPToolAdapterConfig],
):
    """Adapter for MCP tools to make them compatible with AutoGen.

    Args:
        server_params (StdioServerParameters): Parameters for the MCP server connection
        tool (Tool): The MCP tool to wrap
    """

    component_type = "tool"
    component_config_schema = MCPToolAdapterConfig

    def __init__(self, server_params: StdioServerParameters, tool: Tool) -> None:
        self._tool = tool
        self._server_params = server_params

        # Extract name and description
        name = tool.name
        description = tool.description or ""

        # Create the input model from the tool's schema
        input_model = create_model(tool.inputSchema)

        # Use Any as return type since MCP tool returns can vary
        return_type: Type[Any] = object

        super().__init__(input_model, return_type, name, description)

    async def run(self, args: BaseModel, cancellation_token: CancellationToken) -> Any:
        """Execute the MCP tool with the given arguments.

        Args:
            args: The validated input arguments
            cancellation_token: Token for cancelling the operation

        Returns:
            The result from the MCP tool

        Raises:
            Exception: If tool execution fails
        """
        kwargs = args.model_dump()

        try:
            async with stdio_client(self._server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()

                    if cancellation_token.is_cancelled():
                        raise Exception("Operation cancelled")

                    result = await session.call_tool(self._tool.name, kwargs)

                    if result.isError:
                        raise Exception(f"MCP tool execution failed: {result.content}")

                    return result.content
        except Exception as e:
            raise Exception(str(e)) from e

    def _to_config(self) -> MCPToolAdapterConfig:
        return MCPToolAdapterConfig(server_params=self._server_params, tool=self._tool)

    @classmethod
    def _from_config(cls, config: MCPToolAdapterConfig) -> "MCPToolAdapter":
        return cls(server_params=config.server_params, tool=config.tool)
