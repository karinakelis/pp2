def spy_game(list):
    we_need = [0,0,7]
    index = 0
    
    for x in list:
        if list[x] == we_need[index]:
            index+=1
        if we_need[index] == len(list):
            return True
        
        return False
    
list = [1,4,86,6,0,5,0,7]
if True:
    print("Yes")
else:
    print("No")