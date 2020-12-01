# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.


numbers = [1, 2, 3, 4]

#creates a new list but that has no effect on the list passed as an argument:
def chop(li):
    li[1:-1]
    return
print(chop(numbers))

# returns a new list
def middle(li):
    return li[1:-1]
print(middle(numbers))
