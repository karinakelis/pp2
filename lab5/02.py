import re
with open ('row.txt','r', encoding='utf-8') as papka:
   data = papka.read()
def match23(data):
    pattern = r'ab{2,3}'
    match = re.findall(pattern,data)
    print(match)
 
print(match23(data))

