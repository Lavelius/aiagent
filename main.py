import os
from dotenv import load_dotenv
import sys
verbose = '--verbose' in sys.argv
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

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
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python
from functions.call_function import call_function
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python,
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
            tool_response = call_function(function_call, verbose=verbose)
            if verbose:
                print(f"-> {tool_response.parts[0].function_response.response}")
            print(f"\nCalling function: {function_call.name}({function_call.args})")
    print(f"Grandmaster Senpai AI Chatbot: {response.text}")


if __name__ == "__main__":
    main()
