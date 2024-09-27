# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    stripped = line[20:]
    
    number = float(stripped)    
    count += 1
    total += number
print("Average spam confidence:", total/count)
