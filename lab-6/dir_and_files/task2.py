import os


def check_path_access(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists")
        print(f"Readable: {os.access(path, os.R_OK)}")
        print(f"Writable: {os.access(path, os.W_OK)}")
        print(f"Executable: {os.access(path, os.X_OK)}")
    else:
        print(f"Path '{path}' doesn't exist")


check_path_access(input("path to check: "))