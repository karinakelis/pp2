def generate_even_numbers(n):
    """
    A generator function that yields even numbers between 0 and n.
    """
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input())

even_numbers_generator = generate_even_numbers(n)

# Formatting the output as comma-separated values
even_numbers = ", ".join(str(num) for num in even_numbers_generator)
print (even_numbers)
