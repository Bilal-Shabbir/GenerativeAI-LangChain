from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-sonnet-4-5-20250929', temperature=2) # temprature range from 0 to 2, mean creativity.

result = model.invoke('What is the capital of Italy')

print(result.content)