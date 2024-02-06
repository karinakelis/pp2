def solve(numheads,numlegs):
    
    c = (numlegs - 4*numheads)/-2
    r = numheads - c
    return f"Rabits: {int(r)}\nChikens: {int(c)}"
print(solve(35,94))