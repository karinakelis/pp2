import time
import math

def delayed_square_root(number, milliseconds):
    seconds = milliseconds / 1000
    
    time.sleep(seconds)
    
    sqrt_value = math.sqrt(number)
    
    return sqrt_value

number = 25100
milliseconds = 2123

sqrt_value = delayed_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {sqrt_value}")
