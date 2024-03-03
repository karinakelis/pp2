'''Write a Python program to delete file by specified path. 
Before deleting check for access and whether a given path exists or not.
'''
import os

def delete_file_if_possible(file_path):
    
    
    if not os.path.exists(file_path):
        print(f"The file does not exist: {file_path}")
        return
    
    
    if not os.access(file_path, os.W_OK):
        print(f"The file is not writable (no delete permission): {file_path}")
        return
    
    try:
        os.remove(file_path)
        print(f"File successfully deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")

file_path = 'path/to/your/file.txt' 
delete_file_if_possible(file_path)
