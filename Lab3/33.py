
def coding(list):
    for i in range(len(list)- 1):
        if list[i] == 3 and list[i+1]==3:
            return True
        else:
            return False
list = [1,3,3,9,8]
print(coding(list))
