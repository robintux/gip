a = float(input("a: "))
q = float(input("q: "))

if a == 0:
	print(a)
elif -1 < q < 1:
	print(a / (1 - q))
else:
	print("no sum")