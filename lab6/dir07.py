'''Write a Python program to copy the contents of a file to another file
'''
def copy_file(path1,path2):
    try:
        with open (path1,'r') as file1:
            content = file1.read()
        with open (path2,'w') as file2:
            file2.write(content)
    except FileNotFoundError:
        print("mistake")
    except Exception as e:
        print("mistake2")
        
path1 = ("123.txt")
path2 =("789.txt")
copy_file(path1,path2)