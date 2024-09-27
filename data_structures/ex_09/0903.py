# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

file = input('Enter the file name: ')
try:
    opentext = open(file)
except:
    print('File cannot be opened:', file)
    exit()

messages = dict()

for line in opentext:
    if not line.startswith("From"):
        continue
    else:
        words = line.split()
        if len(words) < 3:
            continue
        messages[words[1]] = messages.get(words[1],0) + 1

print(messages)
