# examples/vectorstore_faiss.py
import os
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# Make sure OPENAI_API_KEY is set in your environment
# export OPENAI_API_KEY="sk-..."

def run_vectorstore_example():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    docs = [
        "LangChain is a framework for developing applications powered by language models.",
        "FAISS is a library for efficient similarity search and clustering of dense vectors.",
        "OpenAI provides powerful embeddings which can be used to turn text into vectors.",
    ]

    # Split documents into chunks (simple splitter)
    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    texts = []
    for d in docs:
        texts.extend(splitter.split_text(d))

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts, embeddings)

    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

    question = "What is FAISS used for?"
    answer = qa.run(question)
    print("Question:", question)
    print("Answer:", answer)

if __name__ == "__main__":
    run_vectorstore_example()
