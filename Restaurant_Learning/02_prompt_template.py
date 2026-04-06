"""
Step 2: PromptTemplate
This script introduces PromptTemplate which helps create reusable prompts
with placeholders for dynamic input variables.
"""

from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

from langchain.prompts import PromptTemplate

# Create a reusable prompt template
prompt_template = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

print("Prompt Template Created!")
print(f"Input Variables: {prompt_template.input_variables}")
print(f"Template: {prompt_template.template}")
print("\n" + "="*60 + "\n")

# Format the template with different inputs
cuisines = ['Arabic', 'Chinese', 'French', 'Spanish']
for cuisine in cuisines:
    formatted_prompt = prompt_template.format(cuisine=cuisine)
    print(f"Formatted Prompt for {cuisine}:")
    print(formatted_prompt)
    print()
