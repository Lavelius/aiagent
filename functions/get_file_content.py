import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a file in the specified working directory, ensuring it is a regular file and within the permitted directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read, relative to the working directory. This should be a valid file path and not a directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    """
    Get the content of a file in the specified working directory.
    """
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure abs_file_path is within working_directory
    if os.path.commonpath([abs_file_path, abs_working_directory]) != abs_working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(abs_file_path, 'r') as file:
        content = file.read()
    
    if len(content) > 10000:
        content = content[:10000] + f'...File "{file_path}" truncated at 10000 characters'

    return content