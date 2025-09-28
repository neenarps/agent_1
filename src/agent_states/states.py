from typing import TypedDict, List, Annotated, Literal
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class StockFinderState(TypedDict):
    messages: Annotated[List[BaseMessage],add_messages]