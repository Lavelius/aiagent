import os
from dotenv import load_dotenv
import sys
verbose = '--verbose' in sys.argv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types
messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) < 2:
        print("No input provided.")
        sys.exit(1)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        )
    
    if verbose:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Grandmaster Senpai AI Chatbot: {response.text}")


if __name__ == "__main__":
    main()
