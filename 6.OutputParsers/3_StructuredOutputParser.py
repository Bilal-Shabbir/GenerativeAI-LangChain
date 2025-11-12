from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain import StructuredOutputParser, ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "mistralai/Mistral-7B-Instruct-v0.2", #mistralai/Mistral-7B-Instruct-v0.2
    task = "text-generation"
)

schema = [
    ResponseSchema(name= 'fact_1', description= 'Fact 1 about the topic'), 
    ResponseSchema(name= 'fact_2', description= 'Fact 2 about the topic'), 
    ResponseSchema(name= 'fact_3', description= 'Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template= 'Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}

)

model = ChatHuggingFace(llm=llm)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)

# con: we can ask for structure of json but can't validate. Make llm to give that structure but for age it can be string istead of number
