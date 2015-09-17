def sum_digits_rec(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits_rec(n/10)



    
