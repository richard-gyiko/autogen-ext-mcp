# AutoGen MCP Extension Samples

This directory contains sample code demonstrating how to use the AutoGen MCP Extension.

## Prerequisites

Before running these samples, you'll need:

1. **Python 3.12 or higher**

2. **Install the package with samples dependencies:**
   ```bash
   pip install "autogen-ext-mcp[samples]"
   ```

3. **Install the FileSystem MCP Server:**
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

4. **OpenAI API Key:**
   Create a `.env` file in the samples directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Available Samples

### agent_chat.py

This sample demonstrates:
- Connecting to the FileSystem MCP server
- Listing available MCP tools
- Using an AutoGen agent to interact with the filesystem
- Creating and writing files
- Reading file contents

To run:
```bash
python samples/agent_chat.py
```

The sample will:
1. Connect to the FileSystem MCP server with access to your Desktop
2. Display all available MCP tools and their parameters
3. Create a sample file on your Desktop using the agent

## Troubleshooting

### Common Issues

1. **FileSystem Server Not Found:**
   - Ensure you've installed the server globally with npm
   - On Windows, use `npx.cmd` instead of `npx` in the server parameters

2. **OpenAI API Key Issues:**
   - Verify your API key is correctly set in the `.env` file
   - Make sure the `.env` file is in the same directory as the sample

3. **Permission Issues:**
   - The FileSystem server needs read/write access to the specified directories
   - On Windows, you may need to run the terminal as administrator

### Getting Help

If you encounter issues:
1. Check the [MCP Server documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
2. Open an issue on the [AutoGen MCP Extension repository](https://github.com/your-repo/autogen-ext-mcp)
