# Restaurant Learning Project

A progressive learning project that teaches LangChain fundamentals through the example of building a restaurant name and menu generator.

## Overview

This project is designed as an **educational journey** through LangChain concepts:
1. Basic LLM usage
2. PromptTemplate for reusable prompts
3. LLMChain for combining prompts and LLMs
4. SimpleSequentialChain (and its limitations)
5. SequentialChain (the solution for multiple outputs)

Each step builds upon the previous one, making it perfect for learning LangChain step-by-step.

## Project Structure

```
Restaurant_Learning/
├── 01_basic_llm.py          # Basic LLM calls without chains
├── 02_prompt_template.py    # Introduction to PromptTemplate
├── 03_llm_chain.py          # LLMChain usage
├── 04_simple_sequential_chain.py  # Problem: limitations of SimpleSequentialChain
├── 05_sequential_chain.py   # Solution: SequentialChain with output_keys
├── keys.py                  # OpenAI API key storage
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Key Concepts Learned

### Step 1: Basic LLM
- Direct LLM calls
- Temperature control
- Simple prompt engineering

### Step 2: PromptTemplate
- Reusable prompt templates
- Input variables
- Prompt formatting

### Step 3: LLMChain
- Combining PromptTemplate + LLM
- Cleaner code structure
- Running chains efficiently

### Step 4: SimpleSequentialChain (Problem)
- Chaining multiple LLMChains
- **Limitation**: Only returns final output
- Why it's insufficient for complex tasks

### Step 5: SequentialChain (Solution)
- Multiple inputs and outputs
- `output_key` parameter usage
- Accessing intermediate results
- Building complex workflows

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your OpenAI API key to `keys.py`:
```python
key = "your_openai_api_key_here"
```

## Running Each Step

Run each script sequentially to understand the progression:

```bash
# Step 1: Basic LLM
python 01_basic_llm.py

# Step 2: PromptTemplate
python 02_prompt_template.py

# Step 3: LLMChain
python 03_llm_chain.py

# Step 4: SimpleSequentialChain (shows the problem)
python 04_simple_sequential_chain.py

# Step 5: SequentialChain (shows the solution)
python 05_sequential_chain.py
```

## Expected Output Example

### From 01_basic_llm.py
```
Generated Restaurant Name:
Taj Mahal Maharaja

Italian Restaurant Name: Bella Notte
Mexican Restaurant Name: El Mariachi
...
```

### From 05_sequential_chain.py
```
ARABIC CUISINE:
  Restaurant: Al-Sayidah's Kitchen
  Menu: Hummus, Falafel, Shawarma, Kibbeh, Tabbouleh, Baklava
```

## Configuration

- **Temperature**: Values range from 0.0 to 1.0
  - 0.0 = Deterministic (same output every time)
  - 0.6 = Balanced (creative yet consistent)
  - 1.0 = Maximum randomness

## Learning Path

This project follows Bloom's taxonomy of learning:
1. **Remember**: Basic LLM (01)
2. **Understand**: PromptTemplate and LLMChain (02-03)
3. **Apply**: Simple chains (04)
4. **Analyze**: Understand limitations (04)
5. **Evaluate**: Compare approaches (04 vs 05)
6. **Create**: Build your own sequential chains

## Common Issues

### API Key Error
- Ensure `keys.py` has your actual OpenAI API key
- Check that your API key has valid billing

### Import Errors
- Run `pip install -r requirements.txt` to install dependencies
- Update dependencies if you have version conflicts

## Next Steps

After completing this learning project:
- Explore the [Restaurant Name Generator](../Restaurant_name_menu/) - the production version using these concepts
- Learn about RAG with the [RAG Learning Project](../RAG_Learning_Project/)
- Build your own custom chains combining different concept

## API Costs

Each script call will incur minimal API costs (typically $0.01-$0.05 per run depending on response length).

## Notes

- Keep `keys.py` secure - don't commit it to version control
- These scripts are designed to be run individually for learning
- Each script is self-contained and can be understood independently
- Feel free to modify prompts and experiment with different cuisines!

## Further Reading

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [PromptTemplate Guide](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
- [Chains Documentation](https://python.langchain.com/docs/expression_language/)
