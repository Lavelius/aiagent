import os
import subprocess

from google.genai import types

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory, ensuring it is a valid Python file and within the permitted directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file path to execute, relative to the working directory. This should be a valid Python file.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found'
    if not file_path.endswith('.py'):
        return f"Error: File {file_path} is not a Python file"
    
    try:
        result = subprocess.run(["python3", abs_file_path], cwd=abs_working_directory, capture_output=True,timeout=30, text=True)
    except Exception as e:
        return f'Error: executing Python file: {(e)}'
    if result.returncode != 0:
        return f'Error: Python script execution failed with return code {result.returncode}\nSTDOUT: {result.stdout.decode()}\nSTDERR: {result.stderr.decode()}'
    if result.stdout == None and result.stderr == None:
        return f'No output produced.'
    return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
    