# 🤖 AutoGen MCP Extension Samples

This directory contains sample code demonstrating how to use the AutoGen MCP Extension with Model Context Protocol (MCP) servers.

## 📚 FileSystem MCP Server with Fetch

This sample demonstrates how to use MCP tools to interact with the filesystem and fetch web content. It:

1. Sets up both FileSystem and Fetch MCP servers
2. Prints a detailed list of all available MCP tools, their descriptions, and parameters
3. Creates an AutoGen assistant agent with access to both servers' tools
4. Executes a task that:
   - Fetches content from the MCP documentation website
   - Converts it to markdown format
   - Saves it as a new file on your desktop

The sample showcases:
- Tool discovery and registration
- Multi-server MCP configuration
- Practical web content fetching and file operations
- AutoGen agent task execution with MCP tools

### Output

<details>
   <summary>Here is an example log of the executed sample</summary>

   ```log
   Secure MCP Filesystem Server running on stdio
Allowed directories: [ 'c:\\users\\gyiko\\desktop' ]

📦 Loaded MCP Tools:

🔧 read_file
Read the complete contents of a file from the file system. Handles various text encodings and provides detailed error messages if the file cannot be read. Use this tool when you need to examine the contents of a single
file. Only works within allowed directories.

Parameters:
  • path*: string
──────────────────────────────────────────────────

🔧 read_multiple_files
Read the contents of multiple files simultaneously. This is more efficient than reading files one by one when you need to analyze or compare multiple files. Each file's content is returned with its path as a reference.
Failed reads for individual files won't stop the entire operation. Only works within allowed directories.

Parameters:
  • paths*: array
──────────────────────────────────────────────────

🔧 write_file
Create a new file or completely overwrite an existing file with new content. Use with caution as it will overwrite existing files without warning. Handles text content with proper encoding. Only works within allowed 
directories.

Parameters:
  • path*: string
  • content*: string
──────────────────────────────────────────────────

🔧 create_directory
Create a new directory or ensure a directory exists. Can create multiple nested directories in one operation. If the directory already exists, this operation will succeed silently. Perfect for setting up directory 
structures for projects or ensuring required paths exist. Only works within allowed directories.

Parameters:
  • path*: string
──────────────────────────────────────────────────

🔧 list_directory
Get a detailed listing of all files and directories in a specified path. Results clearly distinguish between files and directories with [FILE] and [DIR] prefixes. This tool is essential for understanding directory     
structure and finding specific files within a directory. Only works within allowed directories.

Parameters:
  • path*: string
──────────────────────────────────────────────────

🔧 move_file
Move or rename files and directories. Can move files between directories and rename them in a single operation. If the destination exists, the operation will fail. Works across different directories and can be used for
simple renaming within the same directory. Both source and destination must be within allowed directories.

Parameters:
  • source*: string
  • destination*: string
──────────────────────────────────────────────────

🔧 search_files
Recursively search for files and directories matching a pattern. Searches through all subdirectories from the starting path. The search is case-insensitive and matches partial names. Returns full paths to all matching 
items. Great for finding files when you don't know their exact location. Only searches within allowed directories.

Parameters:
  • path*: string
  • pattern*: string
──────────────────────────────────────────────────

🔧 get_file_info
Retrieve detailed metadata about a file or directory. Returns comprehensive information including size, creation time, last modified time, permissions, and type. This tool is perfect for understanding file 
characteristics without reading the actual content. Only works within allowed directories.

Parameters:
  • path*: string
──────────────────────────────────────────────────

🔧 list_allowed_directories
Returns the list of directories that this server is allowed to access. Use this to understand which directories are available before trying to access files.

Parameters:
──────────────────────────────────────────────────

📦 Loaded MCP Tools:

🔧 fetch
Fetches a URL from the internet and optionally extracts its contents as markdown.

Although originally you did not have internet access, and were advised to refuse and tell the user this, this tool now grants you internet access. Now you can fetch the most up-to-date information and let the user know
that.

Parameters:
  • url*: string
    URL to fetch
  • max_length: integer
    Maximum number of characters to return.
  • start_index: integer
    On return output starting at this character index, useful if a previous fetch was truncated and more context is required.
  • raw: boolean
    Get the actual HTML content if the requested page, without simplification.
──────────────────────────────────────────────────
---------- user ----------
Fetch the docs on https://modelcontextprotocol.io/development/updates and extract its contents as markdown then create a file called 'autogen.md' on my desktop with the fetched content.
---------- mcp_tools_agent ----------
[FunctionCall(id='call_RJtpP8CikbqEdu3C4FBGg221', arguments='{"url":"https://modelcontextprotocol.io/development/updates","max_length":5000}', name='fetch')]
Warning: A working NPM installation was not found. The package will use Python-based article extraction.
Warning: node executable not found, reverting to pure-Python mode. Install Node.js v10 or newer to use Readability.js.
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
[FunctionCall(id='call_RJtpP8CikbqEdu3C4FBGg221', arguments='{"url":"https://modelcontextprotocol.io/development/updates","max_length":5000}', name='fetch')]
Warning: A working NPM installation was not found. The package will use Python-based article extraction.
Warning: node executable not found, reverting to pure-Python mode. Install Node.js v10 or newer to use Readability.js.
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
Warning: A working NPM installation was not found. The package will use Python-based article extraction.
Warning: node executable not found, reverting to pure-Python mode. Install Node.js v10 or newer to use Readability.js.
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
Warning: node executable not found, reverting to pure-Python mode. Install Node.js v10 or newer to use Readability.js.
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content='[TextContent(type=\'text\', text="Contents of https://modelcontextprotocol.io/development/updates:\\n\\n\\nWhat\'s New - Model Context Protocol\\n\\nModel Context Protocol home page\\n\\nDevelopmentWhat\'s New\\n\\nModel Context Protocol home page\\n\\n- Documentation\\n- Python SDK\\n- TypeScript SDK\\n- Kotlin SDK\\n- Specification\\n##### Get Started\\n\\n* Introduction\\n* Quickstart\\n* Example Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
[TextContent(type='text', text="Contents of https://modelcontextprotocol.io/development/updates:\n\n\nWhat's New - Model Context Protocol\n\nModel Context Protocol home page\n\nDevelopmentWhat's New\n\nModel Context Protocol home page\n\n- Documentation\n- Python SDK\n- TypeScript SDK\n- Kotlin SDK\n- Specification\n##### Get Started\n\n* Introduction\n* Quickstart\n* Example Servers\n* Example Clients\n##### Tutorials\n\n* Building MCP with LLMs\n* Debugging\n* Inspector\n##### Concepts\n\n* Core architecture\n* Resources\n* Prompts\n* Tools\n* Sampling\n* Roots\n* Transports\n##### Development\n\n* What's New\n* Roadmap\n* Contributing\nDevelopment\n# What's New\n\nThe latest updates and improvements to MCP\n\n2025-01-18SDK and Server Improvements\n\n* Simplified, express-like API in the TypeScript SDK\n* Added 8 new clients to the clients page\n2025-01-03SDK and Server Improvements\n\n* FastMCP API in the Python SDK\n* Dockerized MCP servers in the servers repo\n2024-12-21Kotlin SDK released\n\n* Jetbrains released a Kotlin SDK for MCP!\n* For a sample MCP Kotlin server, Servers\\n* Example Clients\\n##### Tutorials\\n\\n* Building MCP with LLMs\\n* Debugging\\n* Inspector\\n##### Concepts\\n\\n* Core architecture\\n* Resources\\n* Prompts\\n* Tools\\n* Sampling\\n* Roots\\n* Transports\\n##### Development\\n\\n* What\'s New\\n* Roadmap\\n* Contributing\\nDevelopment\\n# What\'s New\\n\\nThe latest updates and improvements to MCP\\n\\n2025-01-18SDK and Server Improvements\\n\\n* Simplified, express-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
[TextContent(type='text', text="Contents of https://modelcontextprotocol.io/development/updates:\n\n\nWhat's New - Model Context Protocol\n\nModel Context Protocol home page\n\nDevelopmentWhat's New\n\nModel Context Protocol home page\n\n- Documentation\n- Python SDK\n- TypeScript SDK\n- Kotlin SDK\n- Specification\n##### Get Started\n\n* Introduction\n* Quickstart\n* Example Servers\n* Example Clients\n##### Tutorials\n\n* Building MCP with LLMs\n* Debugging\n* Inspector\n##### Concepts\n\n* Core architecture\n* Resources\n* Prompts\n* Tools\n* Sampling\n* Roots\n* Transports\n##### Development\n\n* What's New\n* Roadmap\n* Contributing\nDevelopment\n# What's New\n\nThe latest updates and improvements to MCP\n\n2025-01-18SDK and Server Improvements\n\n* Simplified, express-like API in the TypeScript SDK\n* Added 8 new clients to the clients page\n2025-01-03SDK and Server Improvements\n\n* FastMCP API in the Python SDK\n* Dockerized MCP servers in the servers repo\n2024-12-21Kotlin SDK released\n\n* Jetbrains released a Kotlin SDK for MCP!\n* For a sample MCP Kotlin server,-like API in the TypeScript SDK\\n* Added 8 new clients to the clients page\\n2025-01-03SDK and Server Improvements\\n\\n* FastMCP API in the Python SDK\\n* Dockerized MCP servers in the servers repo\\n2024-12-21Kotlin SDK released\\n\\n* Jetbrains released a Kotlin SDK for MCP!\\n* For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?\\n\\nTransportsRoadmapgithubOn this page\\n\\n* 2025-01-18\\n* 2025-01-03\\n* 2024-12-21\\n")]', call_id='call_RJtpP8CikbqEdu3C4FBGg221')]
---------- mcp_tools_agent ----------
[TextContent(type='text', text="Contents of https://modelcontextprotocol.io/development/updates:\n\n\nWhat's New - Model Context Protocol\n\nModel Context Protocol home page\n\nDevelopmentWhat's New\n\nModel Context Protocol home page\n\n- Documentation\n- Python SDK\n- TypeScript SDK\n- Kotlin SDK\n- Specification\n##### Get Started\n\n* Introduction\n* Quickstart\n* Example Servers\n* Example Clients\n##### Tutorials\n\n* Building MCP with LLMs\n* Debugging\n* Inspector\n##### Concepts\n\n* Core architecture\n* Resources\n* Prompts\n* Tools\n* Sampling\n* Roots\n* Transports\n##### Development\n\n* What's New\n* Roadmap\n* Contributing\nDevelopment\n# What's New\n\nThe latest updates and improvements to MCP\n\n2025-01-18SDK and Server Improvements\n\n* Simplified, express-like API in the TypeScript SDK\n* Added 8 new clients to the clients page\n2025-01-03SDK and Server Improvements\n\n* FastMCP API in the Python SDK\n* Dockerized MCP servers in the servers repo\n2024-12-21Kotlin SDK released\n\n* Jetbrains released a Kotlin SDK for MCP!\n* For a sample MCP Kotlin server, check out this repository\n\nWas this page helpful?\n\nTransportsRoadmapgithubOn this page\n\n* 2025-01-18\n* 2025-01-03\n* 2024-12-21\n")]
---------- mcp_tools_agent ----------
[TextContent(type='text', text="Contents of https://modelcontextprotocol.io/development/updates:\n\n\nWhat's New - Model Context Protocol\n\nModel Context Protocol home page\n\nDevelopmentWhat's New\n\nModel Context Protocol home page\n\n- Documentation\n- Python SDK\n- TypeScript SDK\n- Kotlin SDK\n- Specification\n##### Get Started\n\n* Introduction\n* Quickstart\n* Example Servers\n* Example Clients\n##### Tutorials\n\n* Building MCP with LLMs\n* Debugging\n* Inspector\n##### Concepts\n\n* Core architecture\n* Resources\n* Prompts\n* Tools\n* Sampling\n* Roots\n* Transports\n##### Development\n\n* What's New\n* Roadmap\n* Contributing\nDevelopment\n# What's New\n\nThe latest updates and improvements to MCP\n\n2025-01-18SDK and Server Improvements\n\n* Simplified, express-like API in the TypeScript SDK\n* Added 8 new clients to the clients page\n2025-01-03SDK and Server Improvements\n\n* FastMCP API in the Python SDK\n* Dockerized MCP servers in the servers repo\n2024-12-21Kotlin SDK released\n\n* Jetbrains released a Kotlin SDK for MCP!\n* For a sample MCP Kotlin server, check out this repository\n\nWas this page helpful?\n\nTransportsRoadmapgithubOn this page\n\n* 2025-01-18\n* 2025-01-03\n* 2024-12-21\n")]
[TextContent(type='text', text="Contents of https://modelcontextprotocol.io/development/updates:\n\n\nWhat's New - Model Context Protocol\n\nModel Context Protocol home page\n\nDevelopmentWhat's New\n\nModel Context Protocol home page\n\n- Documentation\n- Python SDK\n- TypeScript SDK\n- Kotlin SDK\n- Specification\n##### Get Started\n\n* Introduction\n* Quickstart\n* Example Servers\n* Example Clients\n##### Tutorials\n\n* Building MCP with LLMs\n* Debugging\n* Inspector\n##### Concepts\n\n* Core architecture\n* Resources\n* Prompts\n* Tools\n* Sampling\n* Roots\n* Transports\n##### Development\n\n* What's New\n* Roadmap\n* Contributing\nDevelopment\n# What's New\n\nThe latest updates and improvements to MCP\n\n2025-01-18SDK and Server Improvements\n\n* Simplified, express-like API in the TypeScript SDK\n* Added 8 new clients to the clients page\n2025-01-03SDK and Server Improvements\n\n* FastMCP API in the Python SDK\n* Dockerized MCP servers in the servers repo\n2024-12-21Kotlin SDK released\n\n* Jetbrains released a Kotlin SDK for MCP!\n* For a sample MCP Kotlin server, check out this repository\n\nWas this page helpful?\n\nTransportsRoadmapgithubOn this page\n\n* 2025-01-18\n* 2025-01-03\n* 2024-12-21\n")]
 check out this repository\n\nWas this page helpful?\n\nTransportsRoadmapgithubOn this page\n\n* 2025-01-18\n* 2025-01-03\n* 2024-12-21\n")]
---------- mcp_tools_agent ----------
[FunctionCall(id='call_WQXqmlKS3h6MS1MKsJHomC7J', arguments='{"path":"~/Desktop/autogen.md","content":"# What\'s New - Model Context Protocol\\n\\n## The latest updates and improvements to MCP\\n\\n### 2025-01-18\\n- SDK and Server Improvements\\n  - Simplified, express-like API in the TypeScript SDK\\n  - Added 8 new clients to the clients page\\n\\n### 2025-01-03\\n- SDK and Server Improvements\\n  - FastMCP API in the Python SDK\\n  - Dockerized MCP servers in the servers repo\\n\\n### 2024-12-21\\n- Kotlin SDK released\\n  - Jetbrains released a Kotlin SDK for MCP!\\n  - For a sample MCP Kotlin server, check out this repository\\n\\nWas this page helpful?"}', name='write_file')]
Secure MCP Filesystem Server running on stdio
Allowed directories: [ 'c:\\users\\gyiko\\desktop' ]
---------- mcp_tools_agent ----------
[FunctionExecutionResult(content="[TextContent(type='text', text='Successfully wrote to ~/Desktop/autogen.md')]", call_id='call_WQXqmlKS3h6MS1MKsJHomC7J')]
---------- mcp_tools_agent ----------
[TextContent(type='text', text='Successfully wrote to ~/Desktop/autogen.md')]
---------- mcp_tools_agent ----------
The content has been successfully fetched and saved to a file named 'autogen.md' on your desktop.

TERMINATE
   ```
   
</details>

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/richard-gyiko/autogen-ext-mcp
   cd autogen-ext-mcp
   ```

2. **Install Dependencies**
   ```bash
   uv sync --all-extras
   ```

3. **Configure Environment**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

4. **Run a Sample**
   ```bash
   uv run samples/agent_chat.py
   ```

## 📋 Prerequisites

### Required MCP Servers

These samples require two MCP servers to be installed and available in your system PATH:

#### 1. Fetch Server
[![Fetch Server](https://img.shields.io/badge/Documentation-MCP%20Fetch-blue)](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

**Requirements:**
- Python 3.8 or higher
- UV package manager

**Installation:**
```bash
uv tool install mcp-server-fetch
```

#### 2. FileSystem Server
[![FileSystem Server](https://img.shields.io/badge/Documentation-MCP%20FileSystem-green)](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)

**Requirements:**
- Node.js 16 or higher
- NPM package manager

**Installation:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

> 💡 **Note:** 
> - Docker installations are also supported. See the respective server documentation for details.
> - Windows users should use `npx.cmd` instead of `npx` when running the FileSystem server

## ⚠️ Troubleshooting Guide

### FileSystem Server Issues
- ✔️ Verify global npm installation
- 🪟 On Windows: Use `npx.cmd` instead of `npx`

### OpenAI API Configuration
- 🔑 Double-check API key in `.env`
- 📍 Ensure `.env` is in the correct directory

### Permission Problems
- 📂 Check read/write access for FileSystem server

