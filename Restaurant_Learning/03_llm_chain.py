"""
Step 3: LLMChain
This script introduces LLMChain which combines PromptTemplate and LLM.
It's cleaner and more efficient than manually formatting prompts.
"""

from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Create prompt template
prompt_template = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

# Initialize LLM
llm = OpenAI(temperature=0.6)

# Create LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template)

print("LLMChain Created!")
print("This combines PromptTemplate + LLM for seamless execution")
print("\n" + "="*60 + "\n")

# Use the chain with different inputs
cuisines = ['Mexican', 'Thai', 'Greek', 'Portuguese']
for cuisine in cuisines:
    result = chain.run(cuisine)
    print(f"{cuisine} Restaurant Name: {result.strip()}")
    print()
