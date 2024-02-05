def rev(string):
    word = string.split(" ")
    word = word[-1::-1]
    return word
string = input("Write a sentence: ")
print(rev(string))
