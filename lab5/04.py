'''Write a Python program to find the sequences of one upper case letter followed by lower case letters.'''


import re
with open ('row.txt','r', encoding='utf-8') as papka:
   data = papka.read()
def match23(data):
    pattern = r'[A-Z][a-z]+'
    match = re.findall(pattern,data)
    print(match)
 
print(match23(data))
