def my_function():
    print("Hello from a function")
    
    
def my_function():
    print("Hello from a function")
my_function()


def my_function(fname,lname):
    print(fname)
    
    
def my_function(x):
    return x+5


def my_function(*kids):
    print("The youngest child is "  + kids[2])
    
    
def my_function(**kids):
    print("His last name is " + kids["lname"])