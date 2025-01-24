import pytest
from mcp import StdioServerParameters, Tool
from autogen_ext_mcp.tools.adapter import MCPToolAdapter


@pytest.fixture
def sample_tool():
    return Tool(
        name="test_tool",
        description="A test tool",
        inputSchema={
            "type": "object",
            "properties": {"test_param": {"type": "string"}},
            "required": ["test_param"],
        },
    )


@pytest.fixture
def sample_server_params():
    return StdioServerParameters(command="echo", args=["test"])


def test_adapter_config_serialization(sample_tool, sample_server_params):
    # Create original adapter
    original_adapter = MCPToolAdapter(
        server_params=sample_server_params, tool=sample_tool
    )

    # Dump to config
    config = original_adapter.dump_component()

    # Load from config
    loaded_adapter = MCPToolAdapter.load_component(config)

    # Verify the loaded adapter matches the original
    assert loaded_adapter._tool.name == original_adapter._tool.name
    assert loaded_adapter._tool.description == original_adapter._tool.description
    assert loaded_adapter._tool.inputSchema == original_adapter._tool.inputSchema
    assert (
        loaded_adapter._server_params.command == original_adapter._server_params.command
    )
