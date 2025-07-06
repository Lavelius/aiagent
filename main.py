import os
from dotenv import load_dotenv
import sys
verbose = '--verbose' in sys.argv
system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
import functions
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
from google import genai
from google.genai import types
messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]
client = genai.Client(api_key=api_key)

from functions.get_files_info import schema_get_files_info
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def main():
    if len(sys.argv) < 2:
        print("No input provided.")
        sys.exit(1)
    response = client.models.generate_content(
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
        model="gemini-2.0-flash-001",
        contents=messages,
        )
    
    if verbose:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    if hasattr(response, 'function_calls') and response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    print(f"Grandmaster Senpai AI Chatbot: {response.text}")


if __name__ == "__main__":
    main()
