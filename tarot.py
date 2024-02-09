import optparse
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=1)

prompt = ChatPromptTemplate(
    input_variables = ["content"],
    messages = [
        SystemMessage(content = "You are a very intuitive, an expert psychic and accurate tarot card reader. Answer the users questions using tarot cards and provide explanation, guidance and clarity they're seeking for."),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm = llm,
    prompt= prompt,
    verbose=True
)

while True:
    content = input('What is your question?: When you want to end the reading say "Thank you" ')
    if content.lower() in ['thank you', 'thanks'] :
        print('Have a nice day!')
        break
    response = chain.run({'content' : content})
    print (response)
    print ('-' * 50)