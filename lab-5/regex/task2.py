import re

text= input()
pattern = "ab{2,3}"

if re.search(pattern, text):
    print(True)
else:
    print(False)