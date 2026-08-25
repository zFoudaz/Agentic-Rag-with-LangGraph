from graph.state import State
from ingestion import retriever

def retrieve(state:State) -> State:
    question = state.get('question')
    docs = retriever.invoke(question)

    return {
        'documents':docs
    }