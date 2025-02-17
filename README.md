# AutoGen Extension for MCP Tools

![PyPI - Version](https://img.shields.io/pypi/v/autogen-ext-mcp)
[![codecov](https://codecov.io/gh/richard-gyiko/autogen-ext-mcp/graph/badge.svg?token=QDGJDYWLRI)](https://codecov.io/gh/richard-gyiko/autogen-ext-mcp)

## 🚨 **This repository is now archived** 🚨  
The functionality of this project has been integrated directly into the official [`autogen-ext`](https://pypi.org/project/autogen-ext/) package and is available from [`version v0.4.6`](https://github.com/microsoft/autogen/releases/tag/python-v0.4.6).  
You can now use it directly in `autogen-ext` without needing this separate package.

For further updates and improvements, please refer to the official [`autogen`](https://github.com/microsoft/autogen) repository.

# About

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

## Quick Start

```python
from autogen_ext_mcp.tools import mcp_server_tools, StdioServerParams
from pathlib import Path

# Get desktop path cross-platform
desktop_path = str(Path.home() / "Desktop")

# Connect to FileSystem MCP server
server_params = StdioServerParams(
    command="npx",
    args=[
        "-y",
        "@modelcontextprotocol/server-filesystem",
        desktop_path,  # Allow access to Desktop directory
    ]
)

# Get tools
tools = await mcp_server_tools(server_params)

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
