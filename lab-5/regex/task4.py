import re

text = input()
pattern = "[A-Z][a-z]+"

x = re.findall(pattern, text)

print(x)