thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)




# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# adding two sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#second can we list, tuple or dictionary
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)




#Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.






