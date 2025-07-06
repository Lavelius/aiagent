import os


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