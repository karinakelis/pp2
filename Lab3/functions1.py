import math

'''#Exercise 1
def ounces(grams):
  return 28.3495231  * grams

print(ounces(50))



#Exercise 2
def temp(F):
    return (5 / 9) * (F - 32)
print(temp(960))

# Exercise 3
def solve(numheads,numlegs):
    
    c = (numlegs - 4*numheads)/-2
    r = numheads - c
    return f"Rabits: {int(r)}\nChikens: {int(c)}"
print(solve(35,94))


#Exercise 4
def filter_prime(list):
   prime_list = []
   for i in list:
       count = 0
       if i == 0  or i == 1:
           continue
       elif i == 2:
           prime_list.append(i)
           continue
       for j in range(2,i):
           if(i % j == 0):
               count+=1
       if(count == 0):
            prime_list.append(i)
   return prime_list
list = [1,2,3,4,5,6,7,8,9]
print(filter_prime(list))      
       
       
#Exercise 5
def permut(word):
    if len(word) == 1:
        return [word]
    a = permut(word[1:])
    char = word[0]
    result = []
    
    for x in a:
        for i in range(len(x) + 1):
            result.append(x[:i] + char + x[i:])
            
            
    return result
string = input("Write a word: ")
print(permut(string))


#Exercise 6

def rev(string):
    word = string.split(" ")
    word = word[-1::-1]
    return word
string = input("Write a sentence: ")
print(rev(string))



#Exercise 7

def coding(list):
    for i in range(len(list)- 1):
        if list[i] == 3 and list[i+1]==3:
            return True
        else:
            return False
list = [1,3,3,9,8]
print(coding(list))


#Exercise 8

def spy_game(nums):
    target1 = 0
    target2 = 0
    target3 = 0
    for x in nums:
        if x == target1:
            target1 = target2
        elif x == target2:
            target2 = target3
        elif x == target3:
             return True
        else:
            return False 
        
nums = [1,2,4,0,0,7,5]
print(spy_game(nums))'''

 #Exercise 9
 
def sphere(R):
    S = (4/3) * math.pi * R**3
    return S
R = 6
print(sphere(R)) 

#Exercise 10

def unique_list(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
            
    for a in new_list:
        print (a , end = " ")
list = [1,2,3,4,5,4,4,8,8,9,10,5]
print(unique_list(list))

#Exercise 11
 
def Polindrome(string):
    ans = string 
    rev = string[::-1]
     
     
            
        

   


        
        
    