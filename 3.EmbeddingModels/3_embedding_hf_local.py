from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "Rome is the capital of Italy"

vector = embedding.embed_query(text)

print(str(vector))

documents = [
    "Rome is the capital of Italy", 
    "Islamabad is the capital of Pakistan", 
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print("---------------Document embedding---------------")
print(str(result))