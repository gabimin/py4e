# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.


word = input("Type a word: ")
index = 0
while index < len(word):
    index += 1
    print(word[-index])
