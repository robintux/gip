def f1(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s
    
    
def f2(n):
    s = 0
    for i in range(1, n+1):
        s+= i**2
    return s

def f3(n):
    s = 0
    for i in range(1, n+1, 2):
        s += i**(-2)
    return s
        
    
def f(term, start, end, step):
    s = 0
    for i in range(start, end+1, step):
        s += term(i)
    return s
    
