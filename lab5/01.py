import re

def match_ab_pattern(s):
    # Regex pattern: 'a' followed by zero or more 'b's
    pattern = r'ab*'
    
    # Search for the pattern in the string
    if re.search(pattern, s):
        return "Match found"
    else:
        return "No match found"


user_input = input("Enter a string to check: ")


print(match_ab_pattern(user_input))