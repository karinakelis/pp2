'''Write a Python program to write a list to a file.
'''
def write_list(path,list):
    try:
        with open(path,'r') as file:
            for item in list:
                file.write(f"{item}\n")
                
    except Exception as e:
        print(f"there is mistake")
path = ("D:\Distr\System\Desktop\python\python")
list = ["apple","banana","kiwi"]
write_list(path,list)