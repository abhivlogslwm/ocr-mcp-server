from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("OCR-MCP")

@mcp.tool()
async def ping():

    return {
        "status": "success",
        "message": "MCP server working"
    }

if __name__ == "__main__":

    mcp.run(
        transport="sse"
    )