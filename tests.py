from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    try:
        files_info = run_python_file("calculator", "main.py")
        print(files_info)

        files_info = run_python_file("calculator", "tests.py")
        print(files_info)

        files_info = run_python_file("calculator", "../main.py")
        print(files_info)

        files_info = run_python_file("calculator", "nonexistent.py")
        print(files_info)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()