h = float(input("Insert height: "))
w = float(input("Insert width: "))

if h <= 0 or w <= 0:
    print("Height and length must be positive")
else:
    print("Area:", h * w)
    print("Circumference:", 2 * (h + w))
