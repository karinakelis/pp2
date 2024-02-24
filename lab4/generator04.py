'''Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.'''
def square(a,b):
    for i in range(a,b+1):
        yield i**2
        

for num in  square(1,5):
    print(num)
