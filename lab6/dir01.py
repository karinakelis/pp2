'''Write a Python program to list only directories, files and all directories, files in a specified path.
'''
import os
def list_dir(path):
    print("Directories:")
    for entry in os.listdir(path):
        full_path = os.path.join(path,entry)
        if os.path.isdir(full_path):
            print(entry)

def list_files(path):
    print("file:")
    for entry in os.listdir(path):
        full_path = os.path.join(path,entry)
        if os.path.isfile(full_path):
            print(entry)
            
def all(path):
    print("all:")
    for entry in os.listdir(path):
        print(entry)
        
path = ("D:\Distr\System\Desktop\python")
print(list_dir(path))
print(list_files(path))
print(all(path))