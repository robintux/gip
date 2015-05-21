def modulo_iter(a, b):
    while a >= b:
        a -= b
    return a
    
def modulo_rec(a, b):
    if a < b:
        return a
    else:
        return modulo_rec(a-b, b)
