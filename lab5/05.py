'''Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.'''
import re
def match(string):
    pattern = r'^a.*b$'
    if re.search(pattern,string):
        return "match found"
    else:
        return "match not found"
string= input()
print(match(string))