# AutoGen Extension for MCP Tools

This package provides integration between [Microsoft AutoGen](https://microsoft.github.io/autogen/) and [MCP (Multi-Agent Cooperation Protocol)](https://github.com/microsoft/mcp) tools, enabling AutoGen agents to use MCP-based tools in their workflows.

## Installation

```bash
pip install autogen-ext-mcp
```

To run the samples, install with the samples extras:
```bash
pip install "autogen-ext-mcp[samples]"
```

## Features

- Seamless integration of MCP tools with AutoGen agents
- Automatic conversion of MCP tool schemas to AutoGen-compatible formats
- Support for async tool execution
- Built-in cancellation support

## Quick Start

```python
from autogen_ext_mcp.tools import get_tools_from_mcp_server
from mcp import StdioServerParameters

# Connect to MCP server
server_params = StdioServerParameters(
    command=["your-mcp-server-command"],
    args=["--your-args"]
)

# Get tools
tools = await get_tools_from_mcp_server(server_params)

# Use tools with AutoGen agents
# The tools can be passed to any AutoGen agent that supports tool use
```

## Requirements

- Python >=3.12
- autogen-core 0.4.0.dev11
- mcp >=1.1.2

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
