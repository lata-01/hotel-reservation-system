from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from src import config
from src.tools.current_date_tool import CurrentTimeTool
from src.tools.table_availability_tool import GetTableAvailabilityTool
from src.tools.save_booking_tool import SaveBookingTool
from src.tools.join_waitinglist_tool import JoinWaitingListTool


memory = MemorySaver()

model = AzureChatOpenAI(
    azure_endpoint=config.AZURE_ENDPOINT,
    api_key=config.AZURE_OPENAI_API_KEY,
    azure_deployment=config.AZURE_DEPLOYMENT,
    api_version=config.AZURE_API_VERSION,
    temperature=0
)

tools = [
    CurrentTimeTool(),
    GetTableAvailabilityTool(),
    SaveBookingTool(),
    JoinWaitingListTool()

]

agent_executor = create_react_agent(
    model=model,
    tools=tools,
    checkpointer=memory,
)
