import string

def count_case(s):
    upper_case_count = sum(1 for char in s if char in string.ascii_uppercase)
    lower_case_count = sum(1 for char in s if char in string.ascii_lowercase)
    
    print(f"Original String: {s}")
    print(f"Number of Uppercase letters: {upper_case_count}")
    print(f"Number of Lowercase letters: {lower_case_count}")

# Example usage
sample_string = "Hello World"
count_case(sample_string)



