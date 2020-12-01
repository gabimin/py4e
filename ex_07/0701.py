opentext = open('mbox-short.txt')
for line in opentext:
    print(line.rstrip().upper())
