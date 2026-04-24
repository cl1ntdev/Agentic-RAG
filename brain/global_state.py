# i think this is just a waterflow object that can be used by being passed around type shi
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class RAGState(TypedDict):
    question: str
    route_decision: str  # 'local' or 'global'
    retrieved_context: str
    final_answer: str