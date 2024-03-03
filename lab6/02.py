'''Write a Python program to check for access to a specified path. Test the existence, readability, 
writability and executability of the specified path
'''
import os
def check_access(path):
    if os.path.exists(path):
        print(f"Exists: Yes")
    else:
        print(f"Exists: No")
        
    if os.access(path, os.R_OK):
        print(f"Readable: yes")
    else:
        print(f"Readable: no")
        
    if os.access(path,os.W_OK):
        print(f"Writable: yes")
    else:
        print(f"Writable:no")
        
    if os.access(path,os.X_OK):
        print(f"Executable: yes")
    else:
        print(f"Executable: no")
        
path = ("D:\Distr\System\Desktop\python")
check_access(path)