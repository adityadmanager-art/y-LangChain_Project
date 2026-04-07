# Setup Guide

This guide explains how to install dependencies and run the projects in this repository on your local machine.

## Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.8+** — [Download here](https://www.python.org/downloads/)
- **pip** — Python package manager (included with Python)
- **Git** — [Download here](https://git-scm.com/)
- An **OpenAI API key** (or the API key for your preferred LLM provider)

## 1. Clone the Repository

```bash
git clone https://github.com/adityadmanager-art/y-LangChain_Project.git
cd y-LangChain_Project
```

## 2. Create a Virtual Environment

It is strongly recommended to use a virtual environment to avoid dependency conflicts.

```bash
python -m venv venv
```

Activate the virtual environment:

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If a specific project has its own `requirements.txt`, navigate to that folder and run the command there.

## 4. Configure Environment Variables

Create a `.env` file in the root of the repository (or within the project folder) and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never commit your `.env` file to version control. It is already listed in `.gitignore`.

## 5. Run a Project

Navigate to the desired project folder and run the main script:

```bash
cd Restaurant_Learning
python main.py
```

Replace `Restaurant_Learning` and `main.py` with the appropriate folder and script name.

## Troubleshooting

- **Module not found errors:** Ensure your virtual environment is activated and dependencies are installed.
- **API errors:** Double-check that your API key is valid and correctly set in `.env`.
- **Python version issues:** Verify you are using Python 3.8 or above with `python --version`.

---

> For further help, see the [contact page](./contact.md) or open a GitHub issue.
