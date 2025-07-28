from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

restaurant_mcp_server = MCPServerStreamableHTTP("http://127.0.0.1:8001/mcp/")

agent = Agent(
    "openai:gpt-4.1",
    instructions="Answer guest questions about dishes or share the full menu when asked about food.",
    toolsets=[restaurant_mcp_server],
)
app = agent.to_a2a()
