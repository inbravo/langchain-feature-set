# LangChain Examples

This directory contains simple, self-contained examples to help new users get started with LangChain.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key (sign up at https://platform.openai.com/)

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running any examples, you must set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="sk-..."
```

Alternatively, you can create a `.env` file in this directory:

```
OPENAI_API_KEY=sk-...
```

**Important:** Never commit your API key to version control!

## Examples

### 1. basic_qa.py - Basic Question Answering

Demonstrates using an LLM with a PromptTemplate and LLMChain to answer questions.

**Run:**
```bash
python basic_qa.py
```

**What it does:**
- Creates an OpenAI LLM instance
- Defines a prompt template for question answering
- Runs a sample question through the chain
- Prints the answer

### 2. chat_memory.py - Chat with Conversation Memory

Shows how to build a chat-style model with conversation memory so the model can reference earlier messages.

**Run:**
```bash
python chat_memory.py
```

**What it does:**
- Uses ChatOpenAI (chat model)
- Implements ConversationBufferMemory to maintain context
- Demonstrates a multi-turn conversation where the second question references the first

### 3. vectorstore_faiss.py - Vector Store Retrieval QA

Demonstrates creating embeddings, building a FAISS vector store, and performing retrieval-based question answering.

**Run:**
```bash
python vectorstore_faiss.py
```

**What it does:**
- Creates in-memory documents
- Generates embeddings using OpenAI
- Builds a FAISS vector store
- Uses RetrievalQA to answer questions based on the stored documents

## Troubleshooting

- **Missing API Key:** Ensure `OPENAI_API_KEY` is set in your environment
- **Module Not Found:** Make sure you've installed all requirements with `pip install -r requirements.txt`
- **FAISS Installation Issues:** On some platforms, you may need to install `faiss-cpu` separately or use `faiss-gpu` if you have CUDA support

## Next Steps

- Modify the examples to use your own data or questions
- Explore different LangChain models and chains
- Check out the official LangChain documentation: https://python.langchain.com/docs/
