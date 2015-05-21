def product_rec(a,b):
    if b == 1:
        return a
    return a + product_rec(a,b-1)


    
