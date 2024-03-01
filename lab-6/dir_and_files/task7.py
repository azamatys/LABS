def copy_file(path1, path2):
    file1 = open(path1, "r")
    file2 = open(path2, "w")
    file2.write(file1.read())
    file1.close()
    file2.close()

file1 = "/Users/Admin/DocumentsClone/Lab-python/lab-6/dir_and_files/files_7/file1.txt"
file2 = "/Users/Admin/DocumentsClone/Lab-python/lab-6/dir_and_files/files_7/file2.txt"

copy_file(file1, file2)
