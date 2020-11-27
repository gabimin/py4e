confidence = 0
count = 0

try:
    inputfile = input("Enter file name: ")
    openfile = open(inputfile)
except:
    print("Not a valid file name:", inputfile)
    quit()

for line in openfile :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        colonplace = line.find(':')
        number = float(line[colonplace+1:])
        count = count + 1
        confidence = confidence + number

print("Average spam confidence:", confidence / count)
