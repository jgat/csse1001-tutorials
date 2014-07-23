def find_numbers(text):
    """
    Identifies and extracts numbers out of a string, returning them as a list
    of integers.

    find_numbers(str) -> list(int)
    """
    result = []
    for word in text.split():
        if word.isdigit():
            result.append(int(word))
    return result


def find_numbers(text):
    """
    Identifies and extracts numbers out of a string, returning them as a list
    of integers.

    find_numbers(str) -> list(int)
    """
    # -------------------------------------------------------------------------
    # Notice how expressive the list comprehension syntax is, in that it sounds
    # almost exactly the same as you would describe the problem in English.
    # I.e.
    #   Convert each word to an integer, for every word in text split over
    #   spaces, if the word is comprised only of digits.
    # 
    #   int(word)           Convert each word to an integer,
    #   for word            for every word
    #   in text.split()     in text split over spaces
    #   if text.isdigit()   if the word is comprised only of digits.
    # -------------------------------------------------------------------------
    return [int(word) for word in text.split() if word.isdigit()]

###############################################################################

# -----------------------------------------------------------------------------
# The intention of this exercise is not to rewrite the logic for the split
# function, but rather to use the existing string split method. In practise,
# this is excessive, as we could just use split, but for this exercise, it
# serves as a simple example to show the power of lambda functions, which will
# be explained below.
# -----------------------------------------------------------------------------
def separate_comma(s):
    """
    Function to split a string over a comma.

    separate_comma(str) -> list(str)
    """
    return s.split(',')

def separate_semicolon(s):
    """
    Function to split a string over a semicolon.

    separate_semicolon(str) -> list(str)
    """
    return s.split(';')

def separate_pipe(s):
    """
    Function to split a string over a pipe character.

    separate_pipe(str) -> list(str)
    """
    return s.split('|')

# -----------------------------------------------------------------------------
# As the tutorial states, we can notice that the above functions are very
# similar, which is a good indicator that we could generalize these three
# functions into something more abstract.
# 
# As mentioned above, we don't need to reinvent the wheel (in terms of writing
# the split function again), but rather we should utilize the existing method.
# -----------------------------------------------------------------------------
def separate(delim):
    """
    Returns a function that splits a string over an abitrary delimiter.

    separate(str) -> (function(str) -> list(str))
    """
    # Return a function that takes an argument s, which when called will split
    # s over the delimiter specified (i.e. the delim parameter).
    return lambda s: s.split(delim)

# -----------------------------------------------------------------------------
# The usefulness of this more general approach can be seen below, when we
# rewrite our initial three functions making use of the separate function.
#
# The below is equivalent to our initial three functions in every way (except
# perhaps that the below functions are missing a docstring comment).
# 
# As you can see, if you contrast the separate function and the three functions
# below against the initial three, this is a much better approach. While it has
# an extra layer of complexity, in that we had to write a general function, it
# is much simpler to extend. While that may not be as easy to see here, imagine
# if each separate_* function had more than one line of code.
# 
# Or perhaps we wanted to write more separate functions, such as
# separate_fullstop, separate_underscore, separate_hash, etc. Which of the two
# approaches would be easier to extend?
#
# Or perhaps there was a need to modify the separating logic. Which of the two
# approaches would be easier to modify the logic? 
# 
# Or perhaps there was an error in our logic. Which of the two approaches would
# be easier to debug?
#
# In every case, it would certainly be latter over the former.
# -----------------------------------------------------------------------------
separate_comma = separate(',')
separate_semicolon = separate(';')
separate_pipe = separate('|')

###############################################################################

# -----------------------------------------------------------------------------
# The below code is a god example of using a generator to abstract the logic
# behind an abitrarily long list of values. We want to access commands like a
# list, but we cannot use a list, because at the time we start processing the
# first command, we do not know all the commands. We only know all the commands
# once the user has quit (i.e. entered the q command). So we use a generator.
# 
# The Python Visualization Tool is really helpful for understanding how this
# code works (and interacts with itself).
# http://csse1001.uqcloud.net/opt/visualize.html
# -----------------------------------------------------------------------------
def get_commands():
    """
    Generator to continuously prompt the user for commands until they quit.

    get_commands() -> generator(str)
    """
    # Continuously prompt the user for commands, yielding them as we receive
    # them, and finishing when the "q"(uit) command is entered.
    while True:
        cmd = raw_input("Command: ").lower()
        if cmd == 'q':
            break
        yield cmd

def simon_says2():
    magic_word = "simon says "
    # Iterate over each command entered and respond accordingly.
    for cmd in get_commands():
        if cmd.startswith(magic_word):
            print "I will", cmd[len(magic_word):]
        else:
            print "I do nothing"

###############################################################################

# -----------------------------------------------------------------------------
# Recursion is very helpful for this task. The first question that must be
# asked is, What is the base case?
#
# The base case is the simplest form of the problem, for which the answer is
# defined in a straightforward manner (i.e. it is trivial). This is the case
# of the empty list, since it only has one permutation, itself. The argument
# could also be made that the simplest case is a list of length 1, however we
# don't want to unnecessarily restrict our permutations function to lists of
# length >= 1, so we can use the empty list as the base case.
#
# The next question that must be asked, is how can we take a non-base case and
# make it one step closer to the base case?
#
# We could notice that the permutations of the list [1, 2, 3, 4] are the same
# as the permutations of:
#   [1] + permutations of [2, 3, 4]
#   [2] + permutations of [1, 3, 4]
#   [3] + permutations of [1, 2, 4]
#   [4] + permutations of [1, 2, 3]
#
#   (where + represents list concatentation)
# Importantly, the above is reducing this one step closer to the base case, in
# that the length of the list has been decreased by one, which is going towards
# zero.
#
# In general, we can see that for every element in a given list, the
# permutations beginning with that element can be found by prepending (i.e.
# inserting at the beginning) that element to every permutation of every other
# element of the list, excluding the current element.
#
# Combining these two observations together, we can write the below function.
#
# Can you figure out the time complexity of the below function? (Answer below)
# -----------------------------------------------------------------------------
def permutations(xs):
    """
    Generates all permutations of a list.

    permutations(list(*)) -> generator(list(*))
    """
    if not xs:
        # Base case: empty list
        # The empty list only has one permutation, itself.
        yield []
    else:
        # General case: non-empty list
        # Iterate over each element in the list and yield every combination of
        # that element and all the permutations of every other element in the
        # list (i.e. the rest of the list).
        for i, x in enumerate(xs):
            for subperm in permutations(xs[:i]+xs[i+1:]):
                yield [x] + subperm

# -----------------------------------------------------------------------------
# It can be observed that this function is recursively calling itself multiple
# times. It may seem at first glance that because of this, the function
# therefore has exponential time complexity because of this, but it does not.
#
# The function is recursively calling itself n times, where n is the length of
# the list. Each time the function calls itself recursively, it does so with
# n-1 arguments. So the total number of iterations are n(n-1)(n-2)...1, which
# is n! (read "n factorial"). Factorials start out slower, but overall they
# grow even faster that exponentials (with constant bases; i.e. not n^n).
# -----------------------------------------------------------------------------