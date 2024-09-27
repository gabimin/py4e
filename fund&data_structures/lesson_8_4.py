fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line.rstrip()
    lists_words = line.split()
    all_words = lst + lists_words
    for w in all_words:
        if w not in lst:
            lst.append(w)
         
print(sorted(lst))    