import os


def check_path(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists")
        print("File_name:", os.path.basename(path))
        print("Dir_name:", os.path.dirname(path))
    else:
        print(f"Path '{path}' doesn't exist")


check_path(input("path to check: "))