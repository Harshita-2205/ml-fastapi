from tavily import TavilyClient
from tavily.errors import InvalidAPIKeyError
from langchain_google_genai import ChatGoogleGenerativeAI

from .credentials import creds
import os


# Function to validate the Tavily API key
def validate_tavily(tav_api):

    # query = "Who is Elon Musk?"
    # tavily_client=TavilyClient(api_key=tav_api)
    # try:
    #     tavily_client.search(query, max_results=1)
    #     print(tavily_client.search(query, max_results=1))
    #     return "ValidAPI"
    # except InvalidAPIKeyError:
    #     return "InvalidAPI"
    
    return "ValidAPI"

# Function to validate the Gemini API key
def validate_gemini(gemini_api):


    llm_gemini = ChatGoogleGenerativeAI(api_key=gemini_api,
                             model="gemini-2.0-flash-exp",
                             credentials=creds)

    
    try:
        llm_gemini.invoke("Hi")
        return "ValidAPI"
    except:
        return "InvalidAPI"



# # Function to validate the GROQ API key




def validate_keys(tav_api,gemini_api):

    tav_res = validate_tavily(tav_api)
    gemini_res = validate_gemini(gemini_api)
    

    if tav_res == "ValidAPI" and gemini_res == "ValidAPI":
        return "Validated"
    else:
        return "One or more API keys are invalid. Please check and try again."