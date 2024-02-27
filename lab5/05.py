'''Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.'''
import re
with open ('row.txt','r', encoding='utf-8') as papka:
   data = papka.read()
def match23(data):
    pattern = r'a.*b'
    match = re.findall(pattern,data)
    print(match)
 
print(match23(data))

