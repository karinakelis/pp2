'''Write a Python program to count the number of lines in a text file.
'''
def count(path):
    try:
        with open(path, "r") as file:
            file_count = sum(1 for line in file)
            print(f"the file has {file_count} lines")
    except FileNotFoundError:
        print(f"there is smth wrong")
path = ("D:\Distr\System\Desktop\python\python")
count(path)
        
    
        
        