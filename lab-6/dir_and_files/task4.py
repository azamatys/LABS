import os


def count_lines(file):
    f = open(file, 'r')
    lines = len(f.readlines())
    print('Number of lines:', lines)
    f.close()

count_lines("/Users/Admin/DocumentsClone/Lab-python/lab-6/test_for_4.txt")