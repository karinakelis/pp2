'''Write a Python program to replace all occurrences of space, comma, or dot with a colon.'''

import re
with open ('row.txt','r', encoding='utf-8') as papka:
   data = papka.read()
def match23(data):
    pattern = r'[ .,]'
    match = re.findall(pattern,data)
    print(match)
 
print(match23(data))

