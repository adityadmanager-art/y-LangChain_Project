# Restaurant Name Generator

A Streamlit-based application that generates creative restaurant names and menu items based on selected cuisine types using LangChain and OpenAI.

## Overview

This tool uses a sequential chain of prompts to first generate a fancy restaurant name for a given cuisine, then create appropriate menu items for that restaurant.

## Features

- **Cuisine Selection**: Choose from 5 cuisine types (Indian, Mexican, Arabic, Italian, American)
- **AI-Generated Names**: Creates unique, creative restaurant names
- **Menu Suggestions**: Suggests relevant menu items for each restaurant
- **Sequential Chains**: Uses LangChain's SequentialChain for multi-step reasoning
- **Simple UI**: Intuitive Streamlit interface

## Tech Stack

- **Streamlit**: Web UI framework
- **LangChain**: LLM chain orchestration
- **LangChain Community**: OpenAI LLM integration
- **OpenAI**: Language model for generation

## Prerequisites

- Python 3.8+
- OpenAI API key
- LangChain and Streamlit libraries

## Installation

1. Ensure all dependencies are installed:
```bash
pip install streamlit langchain langchain-community openai python-dotenv
```

2. Set up your OpenAI API key in `keys.py`:
```python
key = "your_openai_api_key_here"
```

## Usage

Run the Streamlit application:
```bash
streamlit run main.py
```

### Steps:
1. Open the app in your browser (typically http://localhost:8501)
2. Select a cuisine from the dropdown in the sidebar:
   - Indian
   - Mexican
   - Arabic
   - Italian
   - American
3. The app automatically generates:
   - A fancy restaurant name
   - A list of suggested menu items

## Project Structure

```
Restaurant_name_menu/
├── main.py              # Streamlit UI and app entry point
├── langchain_helper.py  # LangChain chain definitions
├── keys.py              # OpenAI API key storage
└── requirements.txt     # Project dependencies
```

## How It Works

### Chain 1: Restaurant Name Generation
- **Input**: Cuisine type
- **Prompt**: Requests a fancy restaurant name for the given cuisine
- **Output**: Creative restaurant name

### Chain 2: Menu Items Generation
- **Input**: Generated restaurant name
- **Prompt**: Requests menu items for the restaurant
- **Output**: Comma-separated list of menu items

### Sequential Execution
Both chains are combined in a SequentialChain that:
1. Generates the restaurant name first
2. Uses that name to generate menu items
3. Returns both outputs together

## Configuration

- **Temperature**: 0.6 (balanced between creativity and consistency)
- **Model**: OpenAI defaults (GPT-3.5 Turbo or similar)

## File Description

### main.py
- Creates Streamlit UI
- Implements sidebar cuisine selector
- Displays restaurant name and menu items
- Handles user interaction and display formatting

### langchain_helper.py
- Defines `generate_restaurant_name_and_items()` function
- Creates prompt templates for both chains
- Sets up sequential chain execution
- Contains test code in `__main__` block

### keys.py
- Stores OpenAI API key (keep this secure!)

## Notes

- Keep your OpenAI API key secure - don't commit it to version control
- API calls will incur costs based on token usage
- Temperature is set to 0.6 for consistent yet creative results
- Works offline once chains are compiled, but requires online access for API calls

## Future Enhancements

- Add more cuisine options
- Implement cuisine filtering/customization
- Save generated restaurant ideas to a database
- Add price ranges and dietary restrictions
- Implement prompt customization options
