import re

text = input()
pattern = "ab*"

if re.search(pattern, text):
    print(True)
else:
    print(False)