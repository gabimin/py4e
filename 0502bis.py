total = 0
count = 0
max = None
min = None
newNumber = None
while newNumber != "done" :
    newNumber = (input("Enter a number: "))
    if newNumber == "done":
        print(total, count, max, min)
    else:
        try:
            newNumber = float(newNumber)
            total = total + newNumber
            count = count + 1
            if max is None or newNumber > max:
                max = newNumber
            if min is None or newNumber < min:
                min = newNumber
        except:
            print("Invalid input")
