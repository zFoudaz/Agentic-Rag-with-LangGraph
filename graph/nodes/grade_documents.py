from graph.state import State
from chains.retrieve_grader import retrieve_grader

def grade_documents(state:State) -> State:
    question = state.get('question')
    docs = state.get('documents')

    filtered_docs = []
    web_search = False

    for doc in docs:
        is_relevant = retrieve_grader.invoke({
                'question': question,
                'documents': doc.page_content
            }).is_relevant
        if is_relevant:
            filtered_docs.append(doc)
        else:
            web_search = True 
    return{
        'documents': filtered_docs,
        'web_search':web_search
    }
        