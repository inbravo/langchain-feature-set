# examples/chat_memory.py
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Make sure OPENAI_API_KEY is set in your environment
# export OPENAI_API_KEY="sk-..."

def run_chat_memory():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    # Create a chat model instance
    chat = ChatOpenAI(temperature=0)

    # Create conversation memory to preserve context across turns
    memory = ConversationBufferMemory()

    # Create a conversation chain with memory
    conversation = ConversationChain(
        llm=chat,
        memory=memory,
        verbose=False
    )

    # First turn: introduce a topic
    print("=== Turn 1 ===")
    question1 = "My favorite color is blue."
    response1 = conversation.predict(input=question1)
    print(f"User: {question1}")
    print(f"Assistant: {response1}")
    print()

    # Second turn: reference previous context
    print("=== Turn 2 ===")
    question2 = "What did I just tell you about my favorite color?"
    response2 = conversation.predict(input=question2)
    print(f"User: {question2}")
    print(f"Assistant: {response2}")
    print()

    print("Notice how the assistant remembers context from Turn 1 in Turn 2!")

if __name__ == "__main__":
    run_chat_memory()
