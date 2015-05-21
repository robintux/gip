def approx_sqrt(n, max_error):
    n = float(n)
    x = 1
    while abs(x - n/x) > max_error:
        x = (x + n/x) / 2
    return x
