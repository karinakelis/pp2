'''Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path.
'''
import os
def test_path(path):
    if os.path.exists(path):
        print(f"Exists: yes {path}")
        directory, filename = os.path.split(path)
        print(f"directory: {directory}")
        print(f"filename: {filename}")
    else:
        print(f"Exists: no")
        
path = ("D:\Distr\System\Desktop\python")
test_path(path)