# AutoGen Extension for MCP Tools

This package provides integration between [Microsoft AutoGen](https://microsoft.github.io/autogen/) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), enabling AutoGen agents to seamlessly connect with various data sources and tools.

MCP is an open standard that enables secure, two-way connections between AI systems and data sources, replacing fragmented integrations with a single universal protocol. This allows AI assistants to maintain context as they move between different tools and datasets.

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
- Connect to any MCP-compatible data source or tool
- Automatic conversion of MCP tool schemas to AutoGen-compatible formats

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

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [MCP Quickstart Guide](https://modelcontextprotocol.io/quickstart)
- [Pre-built MCP Servers](https://github.com/modelcontextprotocol/servers)

## Requirements

- Python >=3.12
- autogen-core 0.4.0.dev11
- mcp >=1.1.2

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
