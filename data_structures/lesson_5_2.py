largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)    
    except:
        print('Invalid input')
        continue
    if largest == None or num > largest:
        largest = num
    if smallest == None or num < smallest:
        smallest = num
    
print("Maximum is", largest)
print("Minimum is", smallest)