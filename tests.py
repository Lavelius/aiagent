from functions.get_files_info import get_files_info

def main():
    files_info = get_files_info("calculator", ".")
    print(files_info)

    files_info = get_files_info("calculator", "pkg")
    print(files_info)

    files_info = get_files_info("calculator", "/bin")
    print(files_info)

    files_info = get_files_info("calculator", "../")
    print(files_info)




if __name__ == "__main__":
    main()