total = 0
count = 0
average = 0
newNumber = None
while newNumber != "done" :
    newNumber = (input("Enter a number: "))
    if newNumber == "done":
        print(total, count, average)
    else:
        try:
            newNumber = float(newNumber)
            total = total + newNumber
            count = count + 1
            average = total / count
        except:
            print("Invalid input")
