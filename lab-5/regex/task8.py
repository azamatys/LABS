import re

example = "ThisStringAtUppercaseLetters"
pattern = "[A-Z][^A-Z]*"

x = re.findall(pattern, example)
print(x)