from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from models import gpt4_1

SYSTEM_PROMPT = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. "
    "Use three sentences maximum and keep the answer concise. "
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("human","Question: {question} \n\n Context: {context}\n\n Answer:")
    ]
)

generation_chain = prompt | gpt4_1 | StrOutputParser()