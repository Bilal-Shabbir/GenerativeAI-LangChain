from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "mistralai/Mistral-7B-Instruct-v0.2", #mistralai/Mistral-7B-Instruct-v0.2
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt: detailed report

template1 = PromptTemplate(
    template= 'Write a detail report on {topic}', 
    input_variables= ['topic']
)

# 2nd prompt: summary
template2 = PromptTemplate(
    template= 'Write a 5 line summary on following text. /n {text}', 
    input_variables= ['text']
)

parser = StrOutputParser()
# as we are using chains, parser will help us. That's why wee need parser
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)