try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()
if h > 40:
    print(40 * r + (h - 40) * (r * 1.5))
else:
    print(h * r)
