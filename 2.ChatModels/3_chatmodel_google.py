from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash', temperature=2) # temprature range from 0 to 2, mean creativity.

result = model.invoke('What is the capital of Italy')

print(result.content)