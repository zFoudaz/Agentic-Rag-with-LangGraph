from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from graph.chains.models import gpt4_1

class GradeDoc(BaseModel):
    is_relevant: bool = Field(description='is this document related to the question or not')

SYSTEM_PROMPT = (
    "You are a grader assessing relevance of a retrieved document to a user question."
    "If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant."
)

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ('system',SYSTEM_PROMPT),
        ('human','Documents: {documents} \n\n user question: {question}')
    ]
)

retrieve_grader = grade_prompt | gpt4_1.with_structured_output(GradeDoc)