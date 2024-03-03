def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_s == cleaned_s[::-1]

sample_string = "A man, a plan, a canal: Panama"
if is_palindrome(sample_string):
    print(f"'{sample_string}' is a palindrome.")
else:
    print(f"'{sample_string}' is not a palindrome.")
