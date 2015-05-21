def approx_pi(n):
    s = 0
    for i in range(1, n+1):
        s += 1.0/i**2
    return (s*6)**(0.5)
        
