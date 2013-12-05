# Task 1a

print "Hello, World!"

# Task 1b

name = raw_input("What is your name? ")
print "Hello, " + name + "!"

# Task 2

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Probably harder to interpret, but significantly shorter
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Task 3

import random
a = random.randint(10, 99)
b = random.randint(10, 99)
print a, "+", b, "=",
guess = int(raw_input())

if guess == a + b:
    print "Correct!"
else:
    print "No, the correct answer is", a+b
