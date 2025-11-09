from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Babar Azam is one of the greatest batsmen of cricket, known for his beautiful batting style and calm temperament.",
    "Shaheen Afridi is a tall left-arm fast bowler famous for swinging the new ball and taking wickets in the opening overs.",
    "Mohammad Rizwan is a determined wicketkeeper-batsman admired for his consistency, quick running, and positive attitude.",
    "Shadab Khan is a dynamic all-rounder who contributes with leg-spin bowling, sharp fielding, and aggressive batting.",
    "Fakhar Zaman is a fearless opening batsman known for his explosive stroke play and match-winning hundreds.",
    "Haris Rauf is a fiery fast bowler who bowls with great pace and passion, often delivering breakthroughs in crucial moments.",
    "Imam-ul-Haq is a stylish top-order batsman recognized for his solid technique and ability to build long innings.",
    "Naseem Shah is a young and talented fast bowler admired for his smooth action and ability to bowl at high speed.",
    "Sarfraz Ahmed is a former captain of Pakistan who led with energy and helped the team win the 2017 Champions Trophy.",
    "The Pakistan cricket team is known for its unpredictable brilliance, combining raw talent, passion, and flair that inspire fans worldwide."
]

query = 'tell me about Naseem Shah'

document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores =  cosine_similarity([query_embedding], document_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(f"Question: {query}")
print(f"Answer: {documents[index]}")
print(f'Similarity score is:{score}')