def computepay(h,r):
    if h > 40:
        x = ((h - 40) * 0.5 + h ) * r
    else:
        x = h * r
    return x

hour = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

p = computepay(hour,rate)

print("Pay",p)
