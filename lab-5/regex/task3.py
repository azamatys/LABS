import re

text = input()
pattern = "[a-z]+_[a-z]+"

x = re.findall(pattern, text)

print(x)