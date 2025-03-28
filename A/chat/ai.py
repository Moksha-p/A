
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Debugging: Print the key to check if it's being loaded
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Initialize OpenAI client with the correct API key
client = OpenAI(api_key=OPEN_API_KEY)

def get__llm_response(gpt_messages):
    """Fetch response from OpenAI GPT model."""
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Ensure the model name is not a string variable
        messages=gpt_messages
    )

    return completion.choices[0].message.content

# Test environment variable loading
print("OPENAI_API_KEY is set:", bool(OPEN_API_KEY))
