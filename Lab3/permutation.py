def permut(word):
    if len(word) == 1:
        return [word]
    a = permut(word[1:])
    char = word[0]
    result = []
    
    for x in a:
        for i in range(len(x) + 1):
            result.append(x[:i] + char + x[i:])
            
            
    return result
string = input("Write a word: ")
print(permut(string))