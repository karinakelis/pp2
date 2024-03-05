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
        
path1 = ("lab6\goi.txt")
path2 =("lab6\temir.txt")
copy_file(path1,path2)