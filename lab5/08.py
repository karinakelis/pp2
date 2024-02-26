import re

def split_at_uppercase(s):
    # Use a regular expression to find all occurrences of uppercase letters followed by zero or more lowercase letters
    return re.findall(r'[A-Z][a-z]*', s)
input_string = input()
split_strings = split_at_uppercase(input_string)

print(split_strings)
