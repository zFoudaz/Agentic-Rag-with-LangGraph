from chains.generation import generation_chain
from graph.state import State

def geneartion(state:State) -> State:
    question = state.get('question')
    docs = state.get('documents')

    generation = generation_chain.invoke({
        'question':question,
        'context':docs
    })

    return {
        'generation':generation
    }