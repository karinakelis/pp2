#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") 
  
#2
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#3
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#4
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

