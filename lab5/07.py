'''Write a python program to convert snake case string to camel case string.'''
def snake_to_camel(string):
    words = string.split('_')
    camel_word = words[0] + ''.join(word.capitalize()for word in words[1:])
    return camel_word
string = input()
print(snake_to_camel(string))
    