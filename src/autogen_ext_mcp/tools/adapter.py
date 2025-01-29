from typing import Any, Self, Type

from autogen_core import CancellationToken, Component
from autogen_core.tools import BaseTool
from json_schema_to_pydantic import create_model
from mcp import ClientSession, Tool
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.sse import sse_client
from pydantic import BaseModel


class StdioMCPToolAdapterConfig(BaseModel):
    """Configuration for the MCP tool adapter."""

    server_params: StdioServerParameters
    tool: Tool


class StdioMCPToolAdapter(
    BaseTool[BaseModel, Any],
    Component[StdioMCPToolAdapterConfig],
):
    """Adapter for MCP tools to make them compatible with AutoGen.

    Args:
        server_params (StdioServerParameters): Parameters for the MCP server connection
        tool (Tool): The MCP tool to wrap
    """

    component_type = "tool"
    component_config_schema = StdioMCPToolAdapterConfig

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

    def _to_config(self) -> StdioMCPToolAdapterConfig:
        return StdioMCPToolAdapterConfig(
            server_params=self._server_params, tool=self._tool
        )

    @classmethod
    def _from_config(cls, config: StdioMCPToolAdapterConfig) -> Self:
        return cls(server_params=config.server_params, tool=config.tool)


class SseServerParameters(BaseModel):
    """Parameters for connecting to an MCP server over SSE."""

    url: str
    headers: dict[str, Any] | None = None
    timeout: float = 5
    sse_read_timeout: float = 60 * 5


class SseMCPToolAdapterConfig(BaseModel):
    """Configuration for the MCP tool adapter."""

    server_params: SseServerParameters
    tool: Tool


class SseMCPToolAdapter(
    BaseTool[BaseModel, Any],
    Component[SseMCPToolAdapterConfig],
):
    """Adapter for MCP tools to make them compatible with AutoGen.

    Args:
        server_params (SseServerParameters): Parameters for the MCP server connection
        tool (Tool): The MCP tool to wrap
    """

    component_type = "tool"
    component_config_schema = SseMCPToolAdapterConfig

    def __init__(self, server_params: SseServerParameters, tool: Tool) -> None:
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
            async with sse_client(
                self._server_params.url,
                headers=self._server_params.headers,
                timeout=self._server_params.timeout,
                sse_read_timeout=self._server_params.sse_read_timeout,
            ) as (read, write):
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

    def _to_config(self) -> SseMCPToolAdapterConfig:
        return SseMCPToolAdapterConfig(
            server_params=self._server_params, tool=self._tool
        )

    @classmethod
    def _from_config(cls, config: SseMCPToolAdapterConfig) -> Self:
        return cls(server_params=config.server_params, tool=config.tool)
