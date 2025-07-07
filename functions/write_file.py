import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the specified working directory, ensuring it is a valid file path and within the permitted directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory where the file will be written. This should be a relative path.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file. If the file already exists, it will be overwritten.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure abs_file_path is within working_directory
    if os.path.commonpath([abs_file_path, abs_working_directory]) != abs_working_directory:
        raise Exception(f'Error: Cannot write to {file_path} as it is outside the permitted working directory')

    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

    with open(abs_file_path, 'w') as f:
        f.write(content)
        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters written)'