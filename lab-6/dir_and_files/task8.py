import os


def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"The file '{path}' has been successfully deleted.")
        except Exception as e:
            print(f"An error occurred while deleting the file '{path}': {e}")
    else:
        print(f"The file '{path}' does not exist.")


file_path = ""
delete_file(file_path)