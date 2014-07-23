# Task 1a
print "Hello, World!"

# Task 1b
name = raw_input("What is your name? ")
print "Hello, " + name + "!"

# Task 1c
# Each line has the input (following >>>), the output, & then an explanation.

# >>> 3--2
# 5
# Order of operations specifies that the unary - (i.e. sign) happens
# before subtraction, so the result is 3 - (-2) = 5

# >>> 5 / 2
# 2
# Integer division, in Python, is the same as dividing and then rounding down
# to the nearest integer. 5 divided by 2 = 2.5 => 2 (rounded down)

# >>> -5 / 2
# -3
# Similarly, as above, -5 divided by 2 = -2.5 => -3 (rounded down)

# >>> 5.0 / 2
# 2.5
# When either of the operands is a float, floating point division (i.e.
# division with fractions) is used.

# >>> 3.0 - 5 / 2
# 1.0
# Operator precedence dictates that / happens before - (subtraction) (i.e.
# more formally "/ takes precendence over -"), so the result is equivalent to
# 3.0 - (5/2) => 3.0 - 2 => 1.0

# >>> '3' + '12'
# '312'
# The + operator for strings concatenates them (i.e. joins them together).

# >>> 3 + '12'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# A number and a string cannot be added/concatenated.

# >>> 3 * '12'
# '121212'
# Multiplying a number (n) by a string (s), or vice-versa, results in the
# string s being repeated n times.

# >>> 'ba'+'na' * 2
# 'banana'
# Similarly to 3.0 - 5 / 2, * takes precedence over +, so the result is
# equivalent to 'ba' + ('na' * 2) => 'ba' + 'nana' => 'banana'

# >>> 'hello' - 'o'
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# The - operation is not defined for strings.

# >>> 'ababab' / 3
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# Similarly to above, the / operation is not defined for a string and an
# integer.

# >>> 2 ** 3
# 8
# a ** b raises a to the power of b, so 2 ** 3 => 2 to the power of 3.

# >>> 9 ** 1/2
# 4
# Operator precedence dictates that ** happens before /, so the result is
# equivalent to (9 ** 1)/2 => 9/2 => 4 (integer division)

# >>> 11 % 4
# 3
# The modulo operator, a % b (read "a modulo b" or "a mod b"), gives the
# remainder of a divided by b.

# >>> -11 % 4
# 1
# As above, but it must be noted that 0 <= remainder < b (if b is > 0). It
# can easily be calculated by asking, What is the difference between a and
# smallest (i.e. closest to zero) multiple of b less than a. Here b = 4,
# a = -11. The smallest multiple of 4 less than -11 is -12 (= -3 * 4), and
# the difference between -11 and -12 is 1 (= -11 - (-12) => -11 + 12)

# >>> 'Tim' > 'Tom'
# False
# Ordering of strings is determined by position on the ascii table. The
# ordering of letters and numbers is A-Z then a-z then 0-9. Each character is
# compared, and if they are the same, then the next character is compared,
# and so on. First 'T' is compared with 'T'. Since 'T' == 'T', the next
# character from each string is compared (i.e. 'i' and 'o'). 'i' comes before
# 'o' (since they are the same case, and i precedes o in the alphabet), so
# 'i' is less than 'o', which is not greater, so the result is False. If the
# input strings are equal, then greater than or less than would both return
# False.

# >>> 'A' < 'a'
# True
# As above, capitals precede lower case letters, so 'A' comes before 'a', and
# hence 'A' < 'a', so the result is True.

#############################################################################

# Task 2
# Note: iff is read as "if and only if"
def is_leap_year(year):
    """
    Returns True iff year is a leap year.

    is_leap_year(int) -> bool
    """

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

    # -----------------------------------------------------------------------
    # It is important to note that we must consider the most specific case
    # first. This is because, when we check for the year being a multiple of
    # 100, we are implying that the year is not a multiple of 400. If we
    # wrote:
    # if year % 100 == 0:
    #     return False
    # elif year % 400 == 0:
    #     return True
    # etc.
    # then the second case would never happen, because any year that is
    # divisible by 400 would also be divisible by 100, and only one branch
    # in an if/elif/else is executed. To avoid this, we want to say that we
    # only consider the case in which the year is divisible by 100 if it is
    # not also divisible by 100. I.e.
    # if year % 100 == 0 and not(year % 400 == 0):
    #     return False
    # elif year % 400 == 0:
    #     return True
    # etc.
    # 
    # But it should be noted, that if we swap the branches, we will only
    # consider the second case (i.e. year % 100) if the first is not true,
    # so we have not(year % 400 == 0) implicitly in the above solution.
    # -----------------------------------------------------------------------

# Probably harder to interpret, but significantly shorter
def is_leap_year(year):
    """
    Returns True iff year is a leap year.

    is_leap_year(int) -> bool
    """
    # A year is a leap year if it is divisible by four and either is not
    # divisible by 100 or is divisible by 400.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Extension task
# See http://en.wikipedia.org/wiki/Zeller's_congruence
def weekday(day, month, year):
    """
    Returns the day of the week corresponding to day, month and year, with
    Saturday being treated as day 0, Sunday as 1, etc.

    weekday(int, int, int) -> str
    """
    # Jan = 13, Feb = 14, of the previous year, etc.
    if month in (1, 2):
        month += 12
        year -= 1

    h = (day + 26 * (month+1) // 10 + year + year // 4 + 6 * (year // 100) +
         year // 400) % 7

    DAYS = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    return DAYS[h]

#############################################################################

# Task 3

# We need some help from the random library.
import random

# Generate two random integers between 10 and 99.
a = random.randint(10, 99)
b = random.randint(10, 99)

# Print to the user in the format {a} + {b} = 
# A simple way to do this is:
# print a, "+", b, "="
# But the preferred way is:
print '{0} + {1} ='.format(a, b)
# Or even print '{left} + {right} ='.format(left=a, right=b)

# Prompt the user for a result to the above sum, converting it to an integer.
guess = int(raw_input())

if guess == a + b:
    # If the user guessed correctly, tell them so.
    print "Correct!"
else:
    # Otherwise, if the user did not guess correctly, inform them of the
    # correct answer.
    print "No, the correct answer is", a+b
