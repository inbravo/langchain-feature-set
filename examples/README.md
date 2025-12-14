# LangChain Feature Set — Examples

This directory contains a few simple, self-contained LangChain example scripts to help you get started.

## Prerequisites
- Python 3.8+
- An OpenAI API key set in the environment as `OPENAI_API_KEY`

## Quickstart
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .\.venv\Scripts\activate # Windows PowerShell
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="sk-..."  # macOS/Linux
   setx OPENAI_API_KEY "sk-..."    # Windows (restart required)
   ```

4. Run an example:
   ```bash
   python basic_qa.py
   python chat_memory.py
   python vectorstore_faiss.py
   ```

## Notes
- These examples use OpenAI models via the official LangChain integrations. You can swap in other LLM integrations if desired.
- FAISS may require platform-specific wheels (use faiss-cpu on many systems). If FAISS fails to install, consider using an alternate vectorstore or running the example without FAISS.
