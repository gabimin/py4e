h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
if h > 40 :
    print(40 * r + (h - 40) * (r * 1.5))
else:
    print(h * r)
