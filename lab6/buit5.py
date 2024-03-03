def check_all_true(my_tuple):
    return all(my_tuple)


my_tuple1 = (True, 1, "A string", [1, 2])
my_tuple2 = (True, 1, "", [])  

print(check_all_true(my_tuple1))  
print(check_all_true(my_tuple2))  
