def is_power_of_two(a):
    while a > 1 and a % 2 == 0:
        a = a/2
    return a == 1
    
        
