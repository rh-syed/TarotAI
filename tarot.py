from dotenv import load_dotenv, find_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
import json

# Memory
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory


from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


load_dotenv(find_dotenv(), override=True)


def getQAPairs():
    qa_pairs = []
    history = getHistory()

    for item in history:
        if item["type"] == "human":
            question = item["data"]["content"]
        elif item["type"] == "ai":
            answer = item["data"]["content"]
            qa_pairs.append((question, answer))
    return qa_pairs


def getHistory():
    with open("tarot_history.json") as tarot_history:
        history = json.load(tarot_history)
    return history


def consultTarot(question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=1)

    # create memory
    history = FileChatMessageHistory("tarot_history.json")

    memory = ConversationBufferMemory(
        memory_key="chat_history", chat_memory=history, return_messages=True
    )

    # add MessagePlaceholder to the prompt
    prompt = ChatPromptTemplate(
        input_variables=["content"],
        messages=[
            SystemMessage(
                content="You are a very intuitive, an expert psychic and accurate tarot card reader. Answer the users questions using 3 tarot cards (draw more cards if needed) and provide explanation, guidance and clarity they're seeking for."
            ),
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # where the memeory will be stored
            HumanMessagePromptTemplate.from_template("{content}"),
        ],
    )

    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=False)
    response = chain.run({"content": question})

    return response
