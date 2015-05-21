def fib_iter(n):
    if n < 2:
        return n
    else:
        xn_2 = 0
        xn_1 = 1
        for i in range(2, n+1):
            xn = xn_2 + xn_1
            xn_2 = xn_1
            xn_1 = xn
        return xn

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
