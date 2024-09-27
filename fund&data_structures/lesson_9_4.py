name = input("Enter file:")

if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

pares = dict()

for sentence in handle: 
    if sentence == 0 or not sentence.startswith('From'): continue
    else:
        word = sentence.split()
        pares[word[1]] = pares.get(word[1],0) + 1

big_writer = None
big_times = 0
    
for sender, times in pares.items():
    if  times > big_times: 
        big_writer = sender
        big_times = times

print(big_writer, int(big_times/2))