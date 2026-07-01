"""Ticketing agent module"""

from google.adk.agents import LlmAgent

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

from src.core.settings import settings
from src.network_agent.sub_agents.ticketing_agent.prompt import TICKETING_INSTRUCTIONS


mcp_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=settings.MCP_URL,
    ),
    tool_filter=[
        "get_tickets_info",
        "send_sql_command"
    ],

)

ticketing_agent = LlmAgent(
    name="ticketing_agent",
    model=settings.MODEL_NAME,
    description="Get data about tickets",
    instruction=TICKETING_INSTRUCTIONS,
    tools=[
        mcp_toolset,
    ],
)