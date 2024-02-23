import math
#1
def radian(degree):
    x = degree * (3.14/180)
    return x
degree = int(input("Input degree: "))
print("Ouput radian: ", (radian(degree)))

#2
def area(height,base1,base2):
    area =  (base1 + base2)/2 * height
    return area
height = int(input("height: "))
base1 = int(input("Base1: "))
base2 = int(input("Base2: "))
print("Area is: ", area(height,base1,base2))


#3
def polygon(length,num):
    a = length/(2 * math.tan(math.pi/num))
    area1 = (num * length * a)/2
    return area1
length = 25
num = 4
print("The area of regular polygon is: ",polygon(length,num))

def parallel(base,h):
    area2 = h * base 
    return area2
base = int(input("base is: "))
h = int(input("height is:" ))
print("Output: ",parallel(base,h))
    
