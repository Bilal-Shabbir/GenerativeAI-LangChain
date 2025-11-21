from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path= 'Books', 
    glob= '*.pdf' ,  # '*.txt' this patteren depends on which kind of documents we want to load
    loader_cls= PyPDFLoader
)

#docs = loader.load()
docs = loader.lazy_load()
#print(len(docs))

for document in docs:
    print(document.metadata)