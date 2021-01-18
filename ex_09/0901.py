# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

file = input('Enter the file name: ')
try:
    opentext = open(file)
except:
    print('File cannot be opened:', file)
    exit()

raw = []

for line in opentext:
    words = line.split()
    raw =raw+words
lotsOfKeys = dict()

for word in raw:
    lotsOfKeys[word] = "no value"

search = input("Enter a word: ")

if search in lotsOfKeys:
    print(search + " is in " + file)
else:
    print(search + " is not in " + file)
