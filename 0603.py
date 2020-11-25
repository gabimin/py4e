# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(string, char):
    sum = 0
    for i in string:
        if i == char:
            sum = sum + 1
    print(sum)

words = input("Type something: ")
letter = input("Type a letter: ")

count(words, letter)
