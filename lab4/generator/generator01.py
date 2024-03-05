def generator_square(N):
    for i in range(1, N+1):
        yield i**2
        
        
gen = generator_square(5)
for square in gen:
    print(square)


