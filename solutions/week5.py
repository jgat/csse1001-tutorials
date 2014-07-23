# ---------------------------------------------------------------------------
# Provided code is shown first with errors corrected, and correct code is
# shown below.
# ---------------------------------------------------------------------------

def is_prime(n):
    """
    Returns True if n is a prime number.

    is_prime(int) -> bool
    """
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            return False
        else:
            # We cannot say that a number is a prime if it is not divisble by
            # one of the numbers between 2 and itself (inclusive). We can
            # only say that it is a prime once we have checked all numbers
            # between 2 and itself, so this return statement must go outside
            # the loop (i.e. after the loop has finished).
            return True

    # As an aside, when checking whether a number n is a prime, one only
    # needs to check whether the number is divisble by integers between 2 and
    # sqrt(n), not between 2 and n.

def get_primes(n):
    """
    Returns a list of the first n primes.

    get_primes(int) -> list(int)
    """
    # Our result should be a list, since we cannot append to a string.
    primes = ''
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
            # i should be increased regardless of whether it is a prime, so
            # i should be incremented outside of the if block (i.e. the
            # indentation of this line should be decreased by one).
            i += 1

    # This function needs to return the list of primes once finished.
    return primes

# ---------------------------------------------------------------------------
# Correct code:
# ---------------------------------------------------------------------------

def is_prime(n):
    """
    Returns True if n is a prime number.

    is_prime(int) -> bool
    """
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            return False
    return True


def get_primes(n):
    """
    Returns a list of the first n primes.

    get_primes(int) -> list(int)
    """
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

n = int(raw_input("How many primes? "))
print "The first", n, "primes are:", get_primes(n)

# ---------------------------------------------------------------------------

#############################################################################

def find_functions(filename):
    """
    Writes the name of each function defined in a given file to functions.txt

    find_functions(str) -> None
    """

    # Open the input and output files with the appropriate modes
    fin = open(filename, 'rU')
    fout = open('functions.txt', 'w')

    # Iterate over each line in the input file
    for line in fin:
        # If the current line begins with 'def ', then a function is defined
        # on this line.
        if line.startswith('def '):
            # Write the function definition to the output file.
            fout.writeline(line.rstrip())
            # Alternatively, this can also be achieved by printing to the
            # output file, like so:
            # print >> fout, line.rstrip()

    # Make sure to close the input and output files once finished.
    fin.close()
    fout.close()

    # -----------------------------------------------------------------------
    # We could alternatively write this method using with blocks, which
    # would automatically close the files for us at the end of the block.
    #
    # with open(filename, 'rU') as fin:
    #     with open('functions.txt', 'w') as fout:
    #         for line in fin:
    #             if line.startswith('def '):
    #                 print >> fout, line.rstrip()
    # -----------------------------------------------------------------------


def find_functions(filename):
    """
    Returns a list of tuples of the name of each function definition in 
    filename and the line on which it was found, in the form (line, def).

    find_functions(str) -> list( (int, str) )
    """
    # Start with an empty list which will be used to hold the tuples.
    functions = []

    with open(filename, 'rU') as fd:
        # Iterate over each line (with its line number, in the file)
        # Second argument to enumerate begins the count at 1 (since the first
        # line is line 1, not line 0)
        for line_num, line in enumerate(fd, 1):
            if line.startswith('def '):
                # Get the part of the text after 'def '
                line = line.split('def ', 1)[1]
                # There are many ways to achieve this, others include:
                # _, _, line = line.partition('def ')
                # line = line[4:]
                # etc.

                # The name of the function is the part of the line before the
                # opening parenthesis.
                name, _, line = line.partition('(')
                # Note: line is now everything after the opening parenthesis.


                # The arguments come between the opening parenthesis (which 
                # is no longer included in the line) and the closing
                # parenthesis.
                args, _, _ = line.partition(')')

                # We need to convert args to a tuple. Since it is of
                # arbitrary length, we need to build a list and then convert
                # that to a tuple using the tuple method.
                args_list = []
                for arg in args.split(','):
                    args_list.append(arg.strip())

                # As an aside, if we know that each argument is separated by
                # a comma and exactly one space, we could use the following:
                # args = tuple(args.split(', '))

                # As a further aside, the above for loop can be written using
                # list comprehension (introduced later in the course). I.e.
                # args = tuple([arg.strip() for arg in arg.split(',')])

                # Append a tuple with the line number, the name of the
                # function, and its parameters (arguments) to the result.
                functions.append((line_num, name, args))

    return functions
