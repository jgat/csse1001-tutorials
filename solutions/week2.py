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

# Extension task
def weekday(day, month, year):
    # Jan = 13, Feb = 14, of the previous year
    if month in (1, 2):
        month += 12
        year -= 1

    h = (day + 26 * (month+1) // 10 + year + year // 4 + 6 * (year // 100) +
         year // 400) % 7

    DAYS = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    return DAYS[h]

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
