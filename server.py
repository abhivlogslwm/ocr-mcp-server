from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
import uvicorn
import os

mcp = FastMCP("OCR-MCP")

@mcp.tool()
async def ping():

    return {
        "status": "success",
        "message": "MCP server working"
    }

app = FastAPI()

app.mount("/", mcp.sse_app())

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )