from dotenv import load_dotenv
load_dotenv()
import os 
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import AzureOpenAIEmbeddings,AzureChatOpenAI

embedding_model = AzureOpenAIEmbeddings(
        api_key= os.environ['OPENAI_KEY'],
        model="text-embedding-3-small",
        azure_endpoint= os.environ['OPENAI_BASE_URL'],
        api_version='2024-12-01-preview'
    )

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [UnstructuredLoader(web_url=url,chunking_strategy='basic').load() for url in urls]
docs_list = []

docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size = 250,
    chunk_overlap = 0
)

docs_splits = text_splitter.split_documents(docs_list)

# run for the first time only

# vectorstore = Chroma.from_documents(
#     documents=docs_splits,
#     collection_name='rag-chroma',
#     embedding= embedding_model,
#     persist_directory="./.chroma"
# )

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function= embedding_model
).as_retriever()