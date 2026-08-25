from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph,START,END
from graph.nodes import retrieve, grade_documents, websearch, geneartion
from graph.consts import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEBSEARCH
from graph.state import State


def decide_to_generate(state:State):
    if state['web_search']:
        return WEBSEARCH
    else:
        return GENERATE

builder = StateGraph(State)

builder.add_node(RETRIEVE,retrieve)
builder.add_node(GRADE_DOCUMENTS,grade_documents)
builder.add_node(WEBSEARCH,websearch)
builder.add_node(GENERATE,geneartion)

builder.add_edge(START, RETRIEVE)
builder.add_edge(RETRIEVE, GRADE_DOCUMENTS)

builder.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

builder.add_edge(WEBSEARCH, GENERATE)
builder.add_edge(GENERATE, END)

graph = builder.compile()

if __name__ == '__main__':
    graph.get_graph().draw_mermaid_png(output_file_path="graph.png")