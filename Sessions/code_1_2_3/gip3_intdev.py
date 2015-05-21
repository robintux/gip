def int_dev(a, b):
    ans = 0
    while a >= b:
        ans += 1
        a -= b

    return ans
