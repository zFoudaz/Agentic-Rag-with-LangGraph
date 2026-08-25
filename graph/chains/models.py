from langchain_openai import AzureChatOpenAI
import os 

gpt4_1 = AzureChatOpenAI(
    api_key= os.environ['OPENAI_KEY'],
    model='gpt-4.1-mini',
    azure_endpoint= os.environ['OPENAI_BASE_URL'],
    api_version='2024-12-01-preview'
)