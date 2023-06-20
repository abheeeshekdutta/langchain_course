from langchain.llms import OpenAI

from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from dotenv import dotenv_values
from langchain.agents import AgentType

config = dotenv_values("../../.env")

llm = OpenAI(model="text-davinci-003", temperature=0)

# remember to set the environment variables
# “GOOGLE_API_KEY” and “GOOGLE_CSE_ID” to be able to use
# Google Search via API.
search = GoogleSearchAPIWrapper()

tools = [
    Tool(
        name="google-search",
        func=search.run,
        description="useful for when you need to search google to answer questions about current events",
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=6,
)

response = agent("What's the latest news about the Mars rover?")
print(response["output"])


import os

os.environ["GOOGLE_CSE_ID"] = "777a8b57329ac4283"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBXbR-KFxioUdgLyQOGTQnml7AhUsZpG44"
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=search.run,
)

tool.run("Obama's first name?")
