from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

def get_search_tool():
    return GoogleSearchTool()

def get_url_tool():
    return url_context