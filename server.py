from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("OCR-MCP")

@mcp.tool()
async def ping():

    return {
        "status": "success",
        "message": "MCP working"
    }

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port
    )