# LangChain Feature Set — Examples

This directory contains simple, self-contained example scripts that demonstrate common LangChain usage patterns. Use them as quick-start templates to learn LangChain concepts such as prompt templates, conversational memory, embeddings, vectorstores, and retrieval-augmented generation (RAG).

Contents
- basic_qa.py — Simple LLMChain example using a PromptTemplate to answer a single question.
- chat_memory.py — Chat-style interaction using a chat model and ConversationBufferMemory to preserve context across turns.
- vectorstore_faiss.py — Small in-memory example that creates embeddings, builds a FAISS vector store, and runs a RetrievalQA chain.
- requirements.txt — Minimal dependencies to run the examples.

Prerequisites
- Python 3.8 or newer
- An OpenAI API key set as the environment variable OPENAI_API_KEY
  - macOS / Linux: export OPENAI_API_KEY="sk-..."
  - Windows (PowerShell): setx OPENAI_API_KEY "sk-..." (you may need to restart your shell)

Quickstart
1. Clone the repository and change into the project directory.
2. Create and activate a virtual environment:
   - macOS/Linux:
     python -m venv .venv
     source .venv/bin/activate
   - Windows PowerShell:
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r examples/requirements.txt

4. Ensure OPENAI_API_KEY is set (see above).

5. Run an example:
   python examples/basic_qa.py
   python examples/chat_memory.py
   python examples/vectorstore_faiss.py

Example details

basic_qa.py
- Purpose: Demonstrates a basic LLMChain using a PromptTemplate to format a question and ask an LLM.
- What it does: Sends a single question and prints a concise answer.
- Expected output: The sample question and a short answer from the model.

chat_memory.py
- Purpose: Demonstrates a chat-style chain that keeps conversation history in memory.
- What it does: Sends multiple turns to ConversationChain with ConversationBufferMemory so follow-ups can reference previous turns.
- Expected output: Two responses printed; the second response should reflect context from the first.

vectorstore_faiss.py
- Purpose: Demonstrates embeddings, vectorstore creation (FAISS), and retrieval + answer with RetrievalQA.
- What it does: Splits a few in-memory documents into chunks, embeds them, builds an in-memory FAISS index, and runs a retrieval-augmented QA query.
- Expected output: The sample question and an answer built using retrieved document context.

Troubleshooting
- OPENAI_API_KEY not set: All scripts will raise an EnvironmentError if the API key is missing. Make sure you export/set the variable before running.
- FAISS installation issues: On some platforms (notably Windows), installing faiss-cpu may be difficult. If you cannot install FAISS:
  - Use an alternative vectorstore supported by LangChain (e.g., Chroma, Milvus, or a managed vector DB).
  - Run the example on Linux/macOS where faiss-cpu wheels are available.
- Dependency conflicts: If you see version conflicts, create a fresh virtual environment and re-install. Consider pinning library versions in requirements.txt for reproducible behavior.

Customization ideas
- Swap models: The examples use OpenAI integrations (OpenAI, ChatOpenAI, OpenAIEmbeddings). You can replace these with other providers or local LLMs supported by LangChain.
- Change vectorstore: Replace FAISS with another vectorstore backend (Chroma, Milvus, Pinecone, etc.) by changing the vectorstore setup in vectorstore_faiss.py.
- Persistence: The FAISS example keeps the index in-memory. For production use persist the index to disk or use a managed vector DB.

Security and costs
- Do not commit API keys or secrets to the repository.
- Be aware that running these examples will consume tokens on your OpenAI account — monitor usage if you run them repeatedly.

Next steps
- Use these examples as a foundation to build RAG systems, chatbots, and other LangChain-powered applications.
- Add tests, argument parsing, logging, or integrate these examples into a small web service to expose the functionality.

License
- Follow the repository license. These examples are provided as-is for learning and experimentation.
