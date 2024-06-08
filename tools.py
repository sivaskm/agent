from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def web_search(query):
    """A search engine optimized for comprehensive, accurate, and trusted results. Useful for when you need to answer questions about current events. Input should be a search query."""
    return tavily.get_search_context(
        query=query, search_depth="advanced", max_tokens=5000
    )


web_search_tool = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": "Get results from web search",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The name of the topic/query. Give only the main topic's name(e.g. 'Machine Learning')",
                }
            },
            "required": ["query"],
        },
    },
}


available_functions = {
    "web_search": web_search,
}
