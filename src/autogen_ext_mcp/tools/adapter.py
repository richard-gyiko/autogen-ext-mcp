from typing import Any, Type
from autogen_core import CancellationToken
from autogen_core.tools import BaseTool
from json_schema_to_pydantic import create_model
from mcp import ClientSession, StdioServerParameters, stdio_client, Tool
from pydantic import BaseModel


class MCPToolAdapter(BaseTool[BaseModel, Any]):
    """Adapter for MCP tools to make them compatible with AutoGen.

    Args:
        server_params (StdioServerParameters): Parameters for the MCP server connection
        tool (Tool): The MCP tool to wrap
    """

    def __init__(self, server_params: StdioServerParameters, tool: Tool) -> None:
        if not isinstance(server_params, StdioServerParameters):
            raise ValueError(
                "server_params must be an instance of StdioServerParameters"
            )
        if not isinstance(tool, Tool):
            raise ValueError("tool must be an instance of Tool")

        self._tool = tool
        self.server_params = server_params

        # Extract name and description
        name = tool.name
        description = tool.description or ""

        # Validate and extract schema information with detailed errors
        if tool.inputSchema is None:
            raise ValueError(f"Tool {name} has no input schema defined")

        if not isinstance(tool.inputSchema, dict):
            raise ValueError(
                f"Invalid input schema for tool {name}: expected dictionary, got {type(tool.inputSchema)}"
            )

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
            async with stdio_client(self.server_params) as (read, write):
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
