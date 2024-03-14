letters = [chr(i) for i in range(65, 91)]

for x in letters:
    path = (
        "/Users/Admin/DocumentsClone/Lab-python/lab-6/dir_and_files/generated_files_6/"
        + x
        + ".txt"
    )
    my_file = open(path, "w")
    my_file.write("Hello")
    my_file.close()