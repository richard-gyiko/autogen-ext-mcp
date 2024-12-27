# AutoGen Extension for MCP Tools

This package provides integration between [Microsoft AutoGen](https://microsoft.github.io/autogen/) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), enabling AutoGen agents to seamlessly connect with various data sources and tools.

MCP is an open standard that enables secure, two-way connections between AI systems and data sources, replacing fragmented integrations with a single universal protocol. This allows AI assistants to maintain context as they move between different tools and datasets.

## Installation

```bash
pip install autogen-ext-mcp
```

## Features

- Seamless integration of MCP tools with AutoGen agents
- Connect to any MCP-compatible data source or tool
- Automatic conversion of MCP tool schemas to AutoGen-compatible formats

## Prerequisites

Before running the samples, you need to install the FileSystem MCP server:

```bash
npm install -g @modelcontextprotocol/server-filesystem
```

This server provides filesystem operations like reading/writing files, creating directories, etc. See the [FileSystem MCP Server documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) for more details.

## Quick Start

```python
from autogen_ext_mcp.tools import get_tools_from_mcp_server
from mcp import StdioServerParameters
from pathlib import Path

# Get desktop path cross-platform
desktop_path = str(Path.home() / "Desktop")

# Connect to FileSystem MCP server
server_params = StdioServerParameters(
    command="npx",
    args=[
        "-y",
        "@modelcontextprotocol/server-filesystem",
        desktop_path,  # Allow access to Desktop directory
    ]
)

# Get tools
tools = await get_tools_from_mcp_server(server_params)

# Use tools with AutoGen agents
# The tools can be passed to any AutoGen agent that supports tool use
```

## Samples

Check out the [samples directory](samples/) for example code and detailed instructions on getting started with the AutoGen MCP Extension. The samples demonstrate common use cases and best practices for integrating MCP tools with AutoGen agents.

## Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/0.4.0.dev11/index.html)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [MCP Quickstart Guide](https://modelcontextprotocol.io/quickstart)
- [Pre-built MCP Servers](https://github.com/modelcontextprotocol/servers)

## Requirements

- Python >=3.12
- AutoGen >=0.4.0
- mcp >=1.1.2

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
