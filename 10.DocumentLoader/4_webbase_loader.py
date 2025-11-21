from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

url = 'https://www.unieuro.it/online/MacBook/MacBook-Air-13-M4-chip-10-core-CPU-8-core-GPU-16GB-256GB-SSD---Mezzanotte-pidAPLMW123TA?utm_campaign=unieuro_informatica_multi_performance_notebook_pmax_multi_%5Bmixed%5D_vvkb261adc9c2344d8b56c6&gclsrc=aw.ds&gad_source=1&gad_campaignid=19847668032&gbraid=0AAAAADMtsiyagWdgBwfxJuWZiXPPMNiqT&gclid=CjwKCAiAuIDJBhBoEiwAxhgyFpXyBWPehKYxLScUk_1Y5vsHdgGkzVlbNUbtOxOlWd9Owf_HWrYLNhoCfwQQAvD_BwE'
loader = WebBaseLoader(url) # can also provide list of urls

docs = loader.load()  

model = ChatOpenAI()
prompt = PromptTemplate(
    template= 'Answer the following \n {question} from the following text \n {text}', 
    input_variables= ['question', 'text']
)

parser = StrOutputParser()





#print(docs[0].page_content)

chain = prompt | model | parser 

result = chain.invoke({'question': "What is the  product we talking about?", "text": docs[0].page_content})