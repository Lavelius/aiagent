import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        dir_path = os.path.abspath(working_directory)
    else:
        # Prevent absolute paths from escaping working_directory
        dir_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_directory = os.path.abspath(working_directory)

    # Ensure dir_path is within working_directory
    if os.path.commonpath([dir_path, abs_working_directory]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    string_list = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        string_list.append(
            f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
        )
    return "\n".join(string_list)