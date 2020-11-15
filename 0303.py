try:
    s = float(input("Enter score: "))
except:
    s = 1.1
if s < 0.0 or s > 1.0:
    print ("Bad Score")
elif s >= 0.9:
    print ("A")
elif s >= 0.8:
    print ("B")
elif s >= 0.7:
    print ("C")
elif s >= 0.6:
    print ("D")
else:
    print ("F")
