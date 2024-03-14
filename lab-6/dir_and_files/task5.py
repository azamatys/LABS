def write_list_to_file(file_path, mylist):
    file = open(file_path, 'w')

    for item in mylist:
        file.write(str(item) + '\n') 

    file.close()

mylist = [6, 7, 8, 9]
file_path = "/Users/Admin/DocumentsClone/Lab-python/lab-6/dir_and_files/test5.txt"

write_list_to_file(file_path, mylist)