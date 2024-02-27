'''Write a Python program to find sequences of lowercase letters joined with a underscore.'''

import re
with open ('row.txt','r', encoding='utf-8') as papka:
   data = papka.read()
def match23(data):
    pattern = r'[a-z]+_[a-z]+'
    match = re.findall(pattern,data)
    print(match)
 
print(match23(data))






