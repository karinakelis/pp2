import functools
import operator

def multiply_list(numbers):
    result = functools.reduce(operator.mul, numbers, 1)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
print("The result of multiplying all the numbers in the list:", multiply_list(numbers))


# list = [1,2,3,8,2]

# iterator = iter(list)
# mult = next(iterator)
# for i in iterator:
#     mult*=i
# print()