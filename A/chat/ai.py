from decouple import config
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
print(os.getenv("OPENAI_API_KEY"))
client = OpenAI()

OPEN_API_KEY = config("OPENAI_API_KEY",cast=str,default = None)
OPENAI_MODEL = "gpt-4o-mini"

def get_client():
    """Initialize OpenAI client with API key."""
    if not OPEN_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
    
    return OpenAI(api_key=OPEN_API_KEY)

def get__llm_response(gpt_messages):
    client = get_client()
    completion = client.chat.completions.create(
        model="OPENAI_MODEL",
        messages=[{
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }]
    )

    return completion.choices[0].message.content
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# print("API Key:", os.getenv("OPENAI_API_KEY"))
# # Retrieve API key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("Error: OPENAI_API_KEY is missing. Check your .env file.")

# # Correct way to initialize OpenAI client
# client = OpenAI(api_key=OPENAI_API_KEY)

# # Function to fetch response
# def get_llm_response(gpt_messages):
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",  # Use variable, not a string
#         messages=gpt_messages
#     )
#     return completion.choices[0].message.content
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Force load .env file
# dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
# load_dotenv(dotenv_path)
# print("API Key:", os.getenv("OPENAI_API_KEY"))
# # Fetch API key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("❌ ERROR: OPENAI_API_KEY is missing. Check your .env file.")

# # Initialize OpenAI Client
# client = OpenAI(api_key=OPENAI_API_KEY)

# # Function to get response
# def get_llm_response(gpt_messages):
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=gpt_messages
#     )
#     return completion.choices[0].message.content
