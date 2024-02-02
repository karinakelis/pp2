'''def my_function():
    print("Hello from a function")'''
    
def my_function():
    print("Hello Karina")
    
my_function()

def my_function(fname):
    print(fname + " Karina")
    
my_function("Email")
my_function("Kelis")
my_function("Amir")


def my_function(fname,lname):
    print(fname + " " + lname)
my_function("Kelis","Karina")

def my_function(food):
    for x in food:
        print(x)

food = ["plov" , "manty" , "sorpa"]
my_function(food)


'''You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:

'''

def my_function(x, /):
  print(x)

my_function(3)

'''To specify that a function can have only keyword arguments, add *, before the arguments:
'''
def my_function(*, x):
  print(x)

my_function(x = 3)

'''Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
'''

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

