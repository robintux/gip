n = int(input("n = ?\n"))

if n <=0:
    print('Bad input')
else:
    if n == 1:
        xn = 0
    elif n == 2:
        xn = 1
    else:
        xn_2 = 0
        xn_1 = 1
        i = 3
        while i <= n:            
            xn = xn_1 + xn_2
            print(xn_2, xn_1, xn)
            xn_2 = xn_1
            xn_1 = xn
            i += 1 # same as i = i + 1
    print('The', n, 'Fibonacci number is', xn)