'''Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
'''
for i in range (69,91):
    filename = r"chr(i).txt"
    with open(filename,"w") as file:
        file.write(f" {chr(i)}.\n")
print("26 text files have been created.")