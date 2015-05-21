def power_iter(a, b):
    prod = 1
    for i in range(b):
        prod *= a
    return prod

def power_rec(a, b):
    if b == 0:
        return 1
    else:
        return a*power_rec(a, b-1)
