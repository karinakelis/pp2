x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


print(3 << 2)
'''
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100'''



print(100 + 5 * 3)

print(8 >> 4 - 2)

'''
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010'''