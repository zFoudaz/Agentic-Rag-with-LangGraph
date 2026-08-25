from typing import TypedDict, List

class State(TypedDict):
    question: str 
    generation: str
    web_search: bool 
    documents: List[str]