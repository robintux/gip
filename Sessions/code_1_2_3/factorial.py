def factorial_rec(n):
    if n < 2:
        return 1
    else:
        return n * factorial_rec(n - 1)

def factorial_iter(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1        
    return prod
