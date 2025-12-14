# examples/basic_qa.py
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Make sure OPENAI_API_KEY is set in your environment
# export OPENAI_API_KEY="sk-..."

def run_basic_qa():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    # Create an LLM instance. You can change model_name to another OpenAI model or local model integration.
    llm = OpenAI(temperature=0)

    template = """
You are a helpful assistant.

Question: {question}

Answer concisely:
"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    chain = LLMChain(llm=llm, prompt=prompt)

    sample_question = "What is LangChain used for?"
    result = chain.run(question=sample_question)
    print("Question:", sample_question)
    print("Answer:", result)

if __name__ == "__main__":
    run_basic_qa()
