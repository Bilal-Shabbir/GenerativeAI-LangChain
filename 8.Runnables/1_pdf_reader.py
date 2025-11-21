from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai.llms import OpenAI
from dotenv import load_dotenv
import os

# Here I create a simple application that will read document and store it in vector database and later we can query our question from this database. In this file every thing is done with out creating chain.

load_dotenv()

FILE_NAME = 'docs.txt'
file_path = os.path.join(os.getcwd(), FILE_NAME)
loader = TextLoader(file_path)
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap=50)
docs = text_splitter.split_documents(document)

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

retrievers = vectorstore.as_retriever()

query = "what is the key takeaway from the document?"
retrieved_docs = retrievers.invoke(query)

retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

llm = OpenAI( temperature= 0.7)

prompt = f'Based on the following text, answer the question: {query}\n\n{retrieved_text}'

answer = llm.invoke(prompt)

print("Answer:", answer)