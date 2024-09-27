# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0). Each time you call random, you get the next number in a long series. To see a sample, run this loop:

import random
for i in range(10):
    x = random.random()
    print(x)


# The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high, and returns an integer between low and high (including both).

print(random.randint(5, 10))
print(random.randint(5, 10))


# To choose an element from a sequence at random, you can use choice:

t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))
print(random.choice(t))
