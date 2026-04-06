"""
Step 1: Basic LLM Usage
This script demonstrates the most basic usage of LangChain with OpenAI LLM.
Simply ask the LLM to generate text without any complex chains.
"""

from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

from langchain.llms import OpenAI

# Initialize the LLM with a specific temperature
llm = OpenAI(temperature=0.6)

# Make a simple LLM call
response = llm('I want to open a restaurant for Indian food. Suggest a fancy name for this.')
print("Generated Restaurant Name:")
print(response)
print("\n" + "="*60 + "\n")

# Try with different cuisines
cuisines = ['Italian', 'Mexican', 'Arabic', 'American']
for cuisine in cuisines:
    prompt = f"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    name = llm(prompt)
    print(f"{cuisine} Restaurant Name: {name}")
