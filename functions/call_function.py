from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function = function_call_part.name
    args = function_call_part.args
    if function == "get_files_info":
        from functions.get_files_info import get_files_info
        function_results = get_files_info("./calculator",**args)
    elif function == "get_file_content":
        from functions.get_file_content import get_file_content
        function_results = get_file_content("./calculator",**args)
    elif function == "write_file":
        from functions.write_file import write_file
        function_results = write_file("./calculator",**args)
    elif function == "run_python_file":
        from functions.run_python import run_python_file
        function_results = run_python_file("./calculator",**args)
    else:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
    )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_results},
            )
        ],
    )

    
