'''thistuple = ("apple",)
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")


#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


tuple = ("ari", "lana","rih")
if "ari" in tuple:
    print("yes")'''
    

#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

'''x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("cherry", "grape","apple")
y = list(thistuple)
y.append("lemon")
thistuple = tuple(y)
print(thistuple)'''

thistuple = ("mama", "papa","damir")
y = ("amir",)
thistuple += y
print(thistuple)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)   #this will raise an error because the tuple no longer exists
