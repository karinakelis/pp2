'''Write a Python program to replace all occurrences of space, comma, or dot with a colon.'''
import re
def replace(text):
    pattern = r'[ .,]'
    rep = re.sub(pattern,':',text)
    return rep 
text = input()
print(replace(text))