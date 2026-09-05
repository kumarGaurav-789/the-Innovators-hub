#!/usr/bin/env python3
"""
SwasthyaNet - MCP Server Runner
Run this script to expose the SwasthyaNet MCP Server via stdio for:
- Claude Desktop
- Cursor
- Antigravity / Gemini CLI
- Any standard MCP Client
"""

from mcp_server.swasthyanet_mcp import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")
