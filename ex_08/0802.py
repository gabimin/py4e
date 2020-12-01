# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])
#
# Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #if the text file has a line that starts with "From" but has less than 3 words the program can fail
    if len(words) <= 1 : continue
    if words[0] != 'From' : continue
    print(words[2])
