# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

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
        if len(words) < 3: continue
        sender = words[1]
        domain = sender.split("@")
        if domain[1] not in messages:
            messages[domain[1]] = 1
        else:
            messages[domain[1]] += 1

print(messages)
