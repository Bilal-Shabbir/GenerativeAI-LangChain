from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template= 'Classify the follwoing feedback into positive or negative sentiment \n {feedback} \n {format_instruction}', 
    input_variables= ['feedback'], 
    partial_variables= {'format_instruction': parser2.get_format_instructions()}

)

classifer_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template= "Write an appropriate response to this positive feedback \n {feedback}", 
    input_variables= ['feedback']
)
prompt3 = PromptTemplate(
    template= "Write an appropriate response to this negative feedback \n {feedback}", 
    input_variables= ['feedback']
)

"""
structure of branching chain
branch_chain = RunnableBranch(
    (condition1, chain1), 
    (condition2, chain2), 
    default chain
)"""

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser), 
    (lambda x: x.sentiment == 'negative', prompt2 | model | parser), 
    RunnableLambda( lambda x : 'could not find sentiment')
)

chain = classifer_chain | branch_chain

result = chain.invoke({'feedback': 'This is a terrible phone'})
print(result)

chain.get_graph().print_ascii()