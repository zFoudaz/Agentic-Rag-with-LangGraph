from langchain_core.documents import Document
from tavily import TavilyClient
import os 
from graph.state import State


tavily_client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

def websearch(state:State) -> State:
    question = state.get('question')
    documents = state.get('documents')
    response = tavily_client.search(query=question)
    results = response['results']
    full_result = "\n".join([ result['content'] for result in results])
    webresult = Document(page_content=full_result)
    if documents:
        documents.append(webresult)
    else:
        documents = [webresult]
    return {
        'documents':documents
    }