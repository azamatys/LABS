import re

def to_snake(my_string):
    x = re.sub("(.)([A-Z])", r"\1_\2", my_string)
    return x.lower()

example = "helloWorldAndUniverse"
print(to_snake(example))