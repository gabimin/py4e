def bmi(weight, height):
    b = weight/(height * height)
    print(b)
    if b <= 18.5:
        return "Underweight"
    elif b <= 25.0:
        return "Normal"
    elif b <= 30.0:
        return "Overweight"
    elif b > 30:
        return "Obese"
    

print (bmi(73.5, 1.72))