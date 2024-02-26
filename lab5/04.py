'''Write a Python program to find the sequences of one upper case letter followed by lower case letters.'''

import re
def find1(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern,text)
    return matches
text = "This is an Example text with Some Words starting with Uppercase followed by lowercase "
print(find1(text))
