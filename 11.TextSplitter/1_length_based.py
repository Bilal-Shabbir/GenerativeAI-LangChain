from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os
path = os.path.join("C:\\Users\\LogIT\\Desktop\\Books\\dl-curriculum.pdf")
loader = PyPDFLoader(path)
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap = 0, 
    separator=''
)

result = splitter.split_documents(docs)
print(result[0].page_content)
