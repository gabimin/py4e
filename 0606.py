# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods
#
# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
#
# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

#strip

word = "    pineapple    "
newWord = word.strip()
print(newWord)
print("p" + newWord.strip("apple") + "e")
print(newWord.strip("pine") + "e")


#replace

word = "bananas"
print(word.replace("nanas", "identikit"[4:7]))
print(word.replace("ba"[0:2], "peaches"[2]))


# find(sub[, start[, end]])

word = "pineapple"
tree = word[:int(word.find("apple"))]
fruit = word[int(word.find("apple")):]
print("I'm sitting under a", tree, "tree eating an",fruit)
