from mcp.server.fastmcp import FastMCP
import uvicorn
import os

mcp = FastMCP("ocr-mcp-server")

@mcp.tool()
async def ping():

    return {
        "status": "success",
        "message": "MCP Server Working"
    }

app = mcp.streamable_http_app()

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )