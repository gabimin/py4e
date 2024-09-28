try:
    c = input("Celsius temperature: ")
    print("Fahrenheit temperature: " + str( (float(c) * (9 / 5)) + 32) )
except:
    print("Enter a number")
