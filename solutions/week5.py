def is_prime(n):
    """Return True if n is a prime number.

    is_prime(int) -> bool
    """
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """Return a list of the first n primes.

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

###############################################################################

def find_functions(filename):
    fin = open(filename)
    fout = open('functions.txt', 'w')
    for line in fin:
        if line.startswith('def '):
            _, _, line = line.partition('def ')
            name, _, _ = line.partition('(')
            print >> fout, name
    fin.close()
    fout.close()

def find_functions(filename):
    fd = open(filename)
    functions = []
    for lnum, line in enumerate(fd, 1):
        if line.startswith('def '):
            _, _, line = line.partition('def ')
            name, _, line = line.partition('(')
            args, _, _ = line.partition(')')
            args = tuple(args.split(', '))
            functions.append((lnum, name, args))
    return functions
