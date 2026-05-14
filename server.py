from mcp.server.fastmcp import FastMCP

mcp = FastMCP("OCR-MCP")

@mcp.tool()
async def ping():

    return {
        "status": "success",
        "message": "MCP Server Working"
    }

if __name__ == "__main__":

    mcp.run(transport="sse")