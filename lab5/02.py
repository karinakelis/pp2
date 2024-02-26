import re
def match23(string):
    pattern = r'ab{2,3}'
    if re.search(pattern,string):
        return "Match found"
    else:
        return "Match not found"
    
string = input()
print(match23(string))