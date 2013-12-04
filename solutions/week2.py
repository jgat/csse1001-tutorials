# Task 1a

print "Hello, World!"

# Task 1b

name = raw_input("What is your name? ")
print "Hello, " + name + "!"

# Task 2

import random
a = random.randint(10, 99)
b = random.randint(10, 99)
print a, "+", b, "=",
guess = int(raw_input())

if guess == a + b:
    print "Correct!"
else:
    print "No, the correct answer is", a+b
