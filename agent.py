import smolagents
from smolagents import CodeAgent, InferenceClientModel,WebSearchTool
print(smolagents.__version__)

search_tool = WebSearchTool()
print(search_tool("What is the capital of France?"))



