# examples/chat_memory.py
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Make sure OPENAI_API_KEY is set in your environment

def run_chat_with_memory():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")

    chat = ChatOpenAI(temperature=0)
    memory = ConversationBufferMemory()

    # ConversationChain will use the chat model and memory to keep context between turns
    conversation = ConversationChain(llm=chat, memory=memory)

    print(conversation.predict(input="Hi, who won the 2020 US Presidential election?"))
    print(conversation.predict(input="When was that person born?"))
    # Because we used memory, the second question is interpreted in context of the first.

if __name__ == "__main__":
    run_chat_with_memory()
