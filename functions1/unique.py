def unique_list(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
            
    for a in new_list:
        print (a , end = " ")
list = [1,2,3,4,5,4,4,8,8,9,10,5]
print(unique_list(list))
