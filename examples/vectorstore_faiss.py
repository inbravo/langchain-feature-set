# examples/vectorstore_faiss.py
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Make sure OPENAI_API_KEY is set in your environment
# export OPENAI_API_KEY="sk-..."

def run_vectorstore_faiss():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    # Sample documents to embed
    documents = [
        "LangChain is a framework for developing applications powered by language models.",
        "It enables applications that are context-aware and can reason about their responses.",
        "LangChain provides components for working with language models, including prompts, chains, and agents.",
        "Vector stores in LangChain allow you to store and retrieve embeddings efficiently.",
        "FAISS is a library for efficient similarity search and clustering of dense vectors.",
    ]

    # Split documents into chunks (in this case they're already small)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.create_documents(documents)

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    # Build FAISS vector store from documents
    print("Building FAISS vector store...")
    vectorstore = FAISS.from_documents(docs, embeddings)
    print("Vector store created successfully!")
    print()

    # Create a retrieval QA chain
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

    # Run a query
    query = "What is LangChain and what can it do?"
    print(f"Query: {query}")
    result = qa_chain.run(query)
    print(f"Answer: {result}")

if __name__ == "__main__":
    run_vectorstore_faiss()
