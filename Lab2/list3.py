mylist = ["a","b","c"]
for x in mylist:
    print(x)
    
    
mylist = ["a", "b", "c"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i+=1
    
'''A short hand for loop that will print all items in a list:'''

list = ["b","n","m"]
[print(z) for z in list]

list2 = ["banan","apple","cherry"]
newlist = []
for x in list2:
    if "a" in x:
        newlist.append(x)
print(newlist)



'''short version'''

list3 = ["banan","apple","cherry"]
newlist1 = [x for x in list3 if "a" in x]
print(newlist1)

mylist = [x for  x in range(10)]
print(mylist)

mylist = [x for  x in range(10) if x < 5]
print(mylist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse =  True)
print(thislist)

