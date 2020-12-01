max = None
min = None
while True:
    newNumber = input("Enter an integer number or 'done' to finish: ")
    if newNumber == "done" :break
    try:
        newNumber = int(newNumber)
        if max is None or newNumber > max:
            max = newNumber
        if min is None or newNumber < min:
            min = newNumber
    except:
        print("Invalid input")
print ("Maximum is", max)
print ("Minimum is", min)
