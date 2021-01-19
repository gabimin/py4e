# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

file = input('Enter the file name: ')
try:
    opentext = open(file)
except:
    print('File cannot be opened:', file)
    exit()

daysOfWeek = dict()

for line in opentext:
    if not line.startswith("From"):
        continue
    else:
        words = line.split()
        if len(words) < 3:
            continue
        daysOfWeek[words[2]] = daysOfWeek.get(words[2],0) + 1

print(daysOfWeek)
