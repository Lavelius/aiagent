from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    files_info = get_file_content("calculator", "lorem.txt")
    print(files_info)

    files_info = get_file_content("calculator", "main.py")
    print(files_info)

    files_info = get_file_content("calculator", "pkg/calculator.py")
    print(files_info)

    files_info = get_file_content("calculator", "/bin/cat")
    print(files_info)




if __name__ == "__main__":
    main()