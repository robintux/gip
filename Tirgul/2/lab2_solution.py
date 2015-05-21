def dec2bin(n):
    bin_str = ''
    while n > 0:
        bin_str = str(n % 2) + bin_str
        n = n//2
    return bin_str

print('dec2bin')
print('4 is', dec2bin(4))
print('5 is', dec2bin(5))
print('11 is', dec2bin(11))
print('--------------------------------')

def dec2bin_rec(n):
    if n == 0:
        return ''
    return dec2bin_rec(n//2) + str(n%2)

print('dec2bin_rec')
print('4 is', dec2bin_rec(4))
print('5 is', dec2bin_rec(5))
print('11 is', dec2bin_rec(11))
print('--------------------------------')

#-----------------------------------
def str2rle(s):
    if len(s) == 0:
        return []

    rle = []
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            rle.append([s[i-1], count])
            count = 1
        else:
            count += 1

    rle.append([s[-1],count])
    return rle

def rle2str(rle):
    s = ''
    for i in rle:
        s += i[0]*i[1]

    return s

print('str2rle and rle2str')
my_str = 'aaabbbb'
rle = str2rle(my_str)
found = rle2str(rle)
print(my_str, rle, found)

my_str = 'google'
rle = str2rle(my_str)
found = rle2str(rle)
print(my_str, rle, found)
print('--------------------------------')
#--------------------------------               
def reverse_digits(n):
    reverse = 0
    while n > 0:
        reverse = reverse*10 + n%10
        n /= 10
    return reverse

print('reverse_digits')
print('123 -> ', reverse_digits(123))
print('508 -> ', reverse_digits(508))
print('--------------------------------')
#-------------------------------------------------------
def calc_change(total_price, amount_paid, bills, coins):
    print('--------------------')
    print("Price:", total_price)
    print("Cash:", amount_paid)

    change = amount_paid - total_price
    if change < 0:
        print("Not enough cash")
        return
        
    change_lst = []
    for bill in bills[::-1]:
        count = 0
        while change >= bill:
            count += 1
            change -= bill        
        change_lst.append([bill, count])
        
    for coin in coins[::-1]:
        count = 0
        while change >= coin:
            count += 1
            change -= coin        
        change_lst.append([coin, count])

    # output
    for i in change_lst:
        print(i[1],'x',i[0])

    return change_lst

print('calc_change')
bills = [20, 50, 100]
coins = [0.5, 1, 5, 10]
calc_change(9.99, 20, bills, coins)
calc_change(0.3, 1, bills, coins)
calc_change(10, 8, bills, coins)
calc_change(13, 200, bills, coins)
        

        
        
