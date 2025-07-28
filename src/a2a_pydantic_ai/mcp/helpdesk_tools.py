import asyncio
import json
import uuid

from fasta2a.client import A2AClient, Message
from fasta2a.schema import TextPart
from fastmcp import FastMCP

mcp = FastMCP(name="A2A client mcp to connect remotely deployed agents.")

RESTAURANT_AGENT = "http://localhost:8000"


@mcp.tool
async def query_restaurant_agent(query: str):
    """Sends a food or menu-related query to the restaurant agent and returns the result."""
    client = A2AClient(base_url=RESTAURANT_AGENT)
    current_task = {}
    user_msg = Message(
        role="user",
        parts=[TextPart(kind="text", text=query)],
        kind="message",
        message_id=str(uuid.uuid4()),
    )
    print("Sending 'send_task' request to RESTAURANT_AGENT....")
    response = await client.send_message(message=user_msg)
    print("Response from Restaurant agent: ", response)
    task = response["result"]
    task_id = task["id"]

    current_task = task
    final_states = ["completed", "failed", "canceled", "rejected"]
    while current_task["status"]["state"] not in final_states:
        print(
            f"Current Status: {current_task['status']['state']}. Waiting 2 seconds...."
        )
        await asyncio.sleep(2)
        get_response = await client.get_task(task_id)
        print(json.dumps(get_response, indent=2))
        current_task = get_response["result"]

    return current_task["artifacts"][-1]["parts"][-1]["text"]
