from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "mistralai/Mistral-7B-Instruct-v0.2", #mistralai/Mistral-7B-Instruct-v0.2
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

"""template = PromptTemplate(
    template= 'Give me the name, age and city of a fictional person \n {format_instruction}',
   # input_variables=[],
    partial_variables= {'format_instruction': parser.get_format_instructions()}

)"""

template = PromptTemplate(
    template= 'Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}

)

"""prompt = template.format()
result = model.invoke(prompt)
final_result = parser.parse(result.content)"""

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})
print(final_result)

# we can't force output structure i.e maybe we want values as string instead of json or viceversa
# not able to force schema is biggest flaw