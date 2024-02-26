'''Write a Python program to find sequences of lowercase letters joined with a underscore.'''
import re
def find(text):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.search(pattern,text)
    return matches
text = "first_example, anotherExample, yet_another_example."
print(find(text))