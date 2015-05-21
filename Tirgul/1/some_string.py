some_string = input("Give me a string: ")
str_len = len(some_string)
print(str_len % 2 == 0 and some_string[:str_len//2] == some_string[str_len//2:])
