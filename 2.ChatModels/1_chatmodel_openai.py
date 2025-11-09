from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature=2, max_completion_tokens=2) # temprature range from 0 to 2, mean creativity.

result = model.invoke('What is the capital of Italy')

print(result.content)