from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from keys import key
import os

os.environ['OPENAI_API_KEY'] = key

llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1 : Restaurant Name
    Prompt_Template_name = PromptTemplate(
        input_variables= ['cuisine'],
        template= "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    
    name_chain = LLMChain(llm = llm, prompt = Prompt_Template_name, output_key = 'restaurant_name')

    # Chain 2: Menu Items
    Prompt_Template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}."
    )   

    food_items_chain = LLMChain(llm = llm , prompt = Prompt_Template_items, output_key = 'menu_items')
    
    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )
    response = chain({'cuisine' : cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))


