code = ['c','p','q','b','y','h','v','z','t','j','r','f','x','d','k','o','g','a',
        'l','i','u','s','m','w','n','e',' ',',']

secret1 = [8, 15, 26, 3, 25, 26, 15, 10, 26, 24, 15, 8, 26, 8, 15, 26, 3, 25]

secret2 = [6, 25, 24, 19, 27, 26, 6, 19, 13, 19, 27, 26, 6, 19, 0, 19]


def decode(code, num_lst):
    orig_sen = ''
    for num in num_lst:
        orig_sen += code[num]
    return orig_sen

if __name__ == '__main__':
	print(decode(code, secret1))
	print(decode(code, secret2))
    




        
