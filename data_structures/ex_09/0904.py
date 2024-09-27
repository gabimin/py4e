# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

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

maximum = 0
for item in messages:
    if messages[item] > maximum:
        maximum = messages[item]
        sender = item
print(sender, maximum)
