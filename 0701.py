opentext = open('mbox-short.txt')

for line in opentext:
    linestrip = line.rstrip()
    print(linestrip.upper())
