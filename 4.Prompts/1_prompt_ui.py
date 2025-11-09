from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatOpenAI(model = 'gpt-4') # temprature range from 0 to 2, mean creativity.

st.header('Reasearch Tool')
st.subheader("1. Select Paper and Explanation Style")

# Paper Selection (st.selectbox)
paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Select...", 
     "Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)

# Style Selection (st.selectbox)
style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", 
     "Technical", 
     "Code-Oriented", 
     "Mathematical"]
)

# Length Selection (st.selectbox)
length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", 
     "Medium (3-5 paragraphs)", 
     "Long (detailed explanation)"]
)


# template
template = load_prompt('template.json')

# one way to use it. Two invokes 1) template.invoke 2) model.invoke
"""prompt = template.invoke({
    'paper_input' : paper_input, 
    'style_input' : style_input, 
    'length_input' : length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)"""
    

# we can also create chain as follwoing 
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
    'paper_input' : paper_input, 
    'style_input' : style_input, 
    'length_input' : length_input
})
    st.write(result.content)
