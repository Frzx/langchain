from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily = TavilyClient()

@tool
def search(query:str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f'Searching for {query}')
    return tavily.search(query=query)

llm = ChatOpenAI()
tools = [TavilySearch()] # pre-built search tool implemented by tavily team
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": HumanMessage(content="Search 3 job postings for an ai engineer in python and pytorch with 3-5 years of experience in India on linkedIn")}
    )
    print(result)

if __name__ == "__main__":
    main()
