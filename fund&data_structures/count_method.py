#count(substring, start=0, end=None): Returns the number of non-overlapping occurrences of a substring in the string.

word = input('word? ')

print(word.count('a'))
print(word.count('an'))
print(word.count(' '))
print(word.count('')) #vacío dice los espacios entre caracteres... raro...