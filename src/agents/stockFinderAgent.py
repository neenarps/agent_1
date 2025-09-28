from langgraph.graph import StateGraph, START, END
from ..agent_states.states import StockFinderState

## Stock finder agent
stock_finder_agent = StateGraph(StockFinderState)