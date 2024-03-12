'''Write a Python program to write a list to a file.
'''
# def write_list(path,list):
#     try:
#         with open(path,'r') as file:
#             for item in list:
#                 file.write(f"{item}\n")
                
#     except Exception as e:
#         print(f"there is mistake")
# path = ("D:\Distr\System\Desktop\python\python")
# list = ["apple","banana","kiwi"]
# write_list(path,list)


def write_list_to_file(file_path, my_list):
    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Iterate over each element in the list
        for item in my_list:
            # Write the item to the file followed by a newline character
            file.write(f"{item}\n")

# Example usage
my_list = ['apple', 'banana', 'cherry']
file_path = 'my_list_file.txt'
write_list_to_file(file_path, my_list)

print(f"List has been written to {file_path}")
