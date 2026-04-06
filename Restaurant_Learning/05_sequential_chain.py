"""
Step 5: SequentialChain (Solution)
This script shows the solution using SequentialChain with output_key parameters.
It allows us to get outputs from multiple chains and use them in subsequent chains.
"""

from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Initialize LLM
llm = OpenAI(temperature=0.6)

# Chain 1: Restaurant Name with output_key
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

# Chain 2: Menu Items with output_key
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}. Return it as comma separated values."
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

# Create SequentialChain
print("Creating SequentialChain with output_key parameters...")
sequential_chain = SequentialChain(
    chains=[name_chain, food_items_chain],
    input_variables=['cuisine'],
    output_variables=['restaurant_name', 'menu_items'],
    verbose=True
)

print("\n" + "="*60)
print("SequentialChain Output (SOLUTION):")
print("="*60 + "\n")

# Now we get BOTH outputs!
result = sequential_chain({'cuisine': 'Arabic'})

print("\n✅ SUCCESS: We get multiple outputs from SequentialChain!")
print("\nRestaurant Name:", result['restaurant_name'].strip())
print("\nMenu Items:", result['menu_items'].strip())

print("\n" + "="*60)
print("Testing with Multiple Cuisines:")
print("="*60 + "\n")

cuisines = ['Italian', 'Mexican', 'Thai', 'American']
for cuisine in cuisines:
    result = sequential_chain({'cuisine': cuisine})
    print(f"\n{cuisine.upper()} CUISINE:")
    print(f"  Restaurant: {result['restaurant_name'].strip()}")
    print(f"  Menu: {result['menu_items'].strip()}")
