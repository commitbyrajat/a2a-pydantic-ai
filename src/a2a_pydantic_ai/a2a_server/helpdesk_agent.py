from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

helpdesk_mcp_sever = MCPServerStreamableHTTP("http://localhost:8002/mcp/")

agent = Agent(
    "openai:gpt-4.1",
    instructions="You are a polite and helpful virtual hotel helpdesk assistant. Assist guests with bookings, check-in, room services, restaurant info, local guidance, and basic issues; escalate complex or sensitive matters to human staff.",
    toolsets=[helpdesk_mcp_sever],
)
app = agent.to_a2a()
