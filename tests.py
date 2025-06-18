from functions.get_files_info import get_file_content

print(get_file_content("calculator", "main.py"))
print("-----------------------------------------------------------------------")
print(get_file_content("calculator", "pkg/calculator.py"))
print("-----------------------------------------------------------------------")
print(get_file_content("calculator", "/bin/cat"))
print("-----------------------------------------------------------------------")
