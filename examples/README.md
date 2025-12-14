# LangChain Examples

This directory contains simple, focused examples demonstrating core LangChain features. Each script is self-contained and designed to help you quickly understand how to use LangChain for common tasks.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key (set as `OPENAI_API_KEY` environment variable)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="sk-..."
```

Or create a `.env` file in this directory:
```
OPENAI_API_KEY=sk-...
```

## Examples

### 1. basic_qa.py - Basic Question & Answer

A simple example showing how to use LangChain with OpenAI's LLM to answer questions using a prompt template.

**Key concepts:**
- Creating an LLM instance
- Using `PromptTemplate` to structure queries
- Building an `LLMChain` to process questions

**Run:**
```bash
python basic_qa.py
```

**Expected output:**
The script will ask a sample question about LangChain and print the answer.

### 2. chat_memory.py - Conversation with Memory

Demonstrates how to build a conversational agent that remembers context across multiple turns.

**Key concepts:**
- Using `ChatOpenAI` for chat-based interactions
- Implementing `ConversationBufferMemory` to maintain context
- Building multi-turn conversations with `ConversationChain`

**Run:**
```bash
python chat_memory.py
```

**Expected output:**
Two questions are asked in sequence. The second question references the first, showing that the conversation maintains context.

### 3. vectorstore_faiss.py - Vector Store with FAISS

Shows how to use FAISS for semantic search and retrieval-augmented generation (RAG).

**Key concepts:**
- Creating embeddings with `OpenAIEmbeddings`
- Building a vector store with FAISS
- Using `RetrievalQA` to answer questions based on document context

**Run:**
```bash
python vectorstore_faiss.py
```

**Expected output:**
A question is answered using information retrieved from the vector store.

## Quickstart

To quickly test all examples:

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY="sk-..."

# Run each example
python basic_qa.py
python chat_memory.py
python vectorstore_faiss.py
```

## Troubleshooting

### OPENAI_API_KEY not set
If you see `EnvironmentError: OPENAI_API_KEY environment variable not set`, make sure you've exported your API key:
```bash
export OPENAI_API_KEY="sk-..."
```

### FAISS installation issues
FAISS may require platform-specific installation. If `pip install faiss-cpu` fails:
- On macOS: Try `conda install -c pytorch faiss-cpu`
- On Linux: Ensure you have the appropriate build tools installed
- On Windows: Consider using conda or pre-built wheels

For more information, see the [FAISS installation guide](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md).

### Import errors
If you encounter import errors related to LangChain modules, ensure you have the latest version:
```bash
pip install --upgrade langchain openai
```

### Rate limiting
If you hit OpenAI rate limits, you may need to:
- Wait before retrying
- Reduce the frequency of API calls
- Upgrade your OpenAI API plan

## Customization Ideas

- **Change the model**: Modify `model_name` parameter in `OpenAI()` or `ChatOpenAI()` to use different models (e.g., `gpt-4`, `gpt-3.5-turbo`)
- **Adjust temperature**: Change the `temperature` parameter to control response randomness (0 = deterministic, 1 = creative)
- **Add more documents**: Extend the documents list in `vectorstore_faiss.py` with your own text
- **Use local models**: Integrate local LLMs using LangChain's HuggingFace or LlamaCpp integrations
- **Persist vector stores**: Save and load FAISS indices to disk for reuse
- **Add more memory types**: Try `ConversationSummaryMemory` or `ConversationBufferWindowMemory`

## Security and Costs

- **Keep your API key secure**: Never commit API keys to version control
- **Monitor usage**: Each API call costs money. Check your OpenAI dashboard regularly
- **Use environment variables**: Always load API keys from environment variables or secure vaults
- **Test with small datasets**: Start with small examples before scaling up to avoid unexpected costs

## Further Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss/wiki)

## Contributing

Feel free to add more examples or improve existing ones! Keep examples simple, focused, and well-documented.
