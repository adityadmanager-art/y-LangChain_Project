"""
Step 4: SimpleSequentialChain (Problem Demo)
This script shows the limitation of SimpleSequentialChain:
It only returns the output of the final chain, losing intermediate results.
"""

from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

# Initialize LLM
llm = OpenAI(temperature=0.5)

# Chain 1: Restaurant Name
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

# Chain 2: Menu Items
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}. Return it as comma separated values."
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)

# Create SimpleSequentialChain
print("Creating SimpleSequentialChain...")
simple_chain = SimpleSequentialChain(chains=[name_chain, food_items_chain])

print("\n" + "="*60)
print("SimpleSequentialChain Output (PROBLEM):")
print("="*60 + "\n")

# The issue: SimpleSequentialChain only returns the FINAL output
result = simple_chain.run('Indian')

print("Output from SimpleSequentialChain:")
print(result)
print("\n⚠️  PROBLEM: We only get the menu items, NOT the restaurant name!")
print("This is because SimpleSequentialChain only returns the output of the last chain.")
