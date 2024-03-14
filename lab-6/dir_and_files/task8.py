import os

def delete_file(path):

    if os.path.exists(path):

        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' has been deleted.")
        else:
            print(f"Unable to delete file '{path}'.")

    else:
        print(f"File '{path}' doesn't exist.")

file_path = "/Users/Admin/DocumentsClone/Lab-python/lab-6/dir_and_files/files_8/delete_file.txt"
delete_file(file_path)