from langchain_openai.llms import OpenAI
from langchain_community.chains import PebbloRetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS, PGVector
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai.llms import OpenAI
from langchain_classic.chains import RetrievalQA
#from langchain_community.chains.pebblo_retrieval.base import PebbloRetrievalQA
from dotenv import load_dotenv
import os

# here I implement same document reader application but using chains.

os.environ["PWD"] = os.getcwd()

load_dotenv()

FILE_NAME = 'docs.txt'
file_path = os.path.join(os.getcwd(), FILE_NAME)
loader = TextLoader(file_path)
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap=50)
docs = text_splitter.split_documents(document)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

retrievers = vectorstore.as_retriever()
llm = OpenAI()

qa_chian = RetrievalQA.from_chain_type(llm=llm, retriever=retrievers)
query = 'What is the key takeaways form the document?'

answer = qa_chian.invoke(query)
print(answer)