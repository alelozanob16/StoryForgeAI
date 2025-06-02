from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()
# Example usage of the SerperDevTool to perform a search query
serper_dev_tool = SerperDevTool(
    api_key=os.getenv("SERPER_API_KEY"),
    search_engine="google",
    search_type="search",
)

result = serper_dev_tool.run(
    query="What is the capital of France?",
    num_results=1,
)
print(f"Search Results: {result}")