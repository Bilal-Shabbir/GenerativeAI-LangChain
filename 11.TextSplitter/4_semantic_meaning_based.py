from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), 
    breakpoint_threshold_type= 'standard_deviation', 
    breakpoint_threshold_amount=0.5
)
text = """
The final of the UEFA Champions League is one of the most-watched annual sporting events worldwide, often attracting a global audience exceeding 400 million viewers.Farmers cultivate food. The vast majority of agricultural production in North America relies on large-scale crop rotation programs to maintain soil health and prevent nutrient depletion over time.

Deep-sea exploration is a rapidly expanding field, utilizing remotely operated vehicles (ROVs) and autonomous underwater vehicles (AUVs) to map the vast and poorly understood abyssal zones. These zones, existing below 1,000 meters, host unique extremophile life forms and possess geological features, such as hydrothermal vents, that shed light on Earth's own formation. The challenges remain immense due to the extreme pressure, lack of light, and cold temperatures, making the deep sea one of the last true frontiers for scientific discovery.
"""

docs = text_splitter.create_documents([text])
print(len(docs))
print(docs)