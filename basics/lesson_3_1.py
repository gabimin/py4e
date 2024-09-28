h = float(input("Hours: "))
r = float(input("Rate: "))
if h > 40:
    p = (h-40) * 1.5 * r + r * 40
    print(p)
else:
    print(h * r)