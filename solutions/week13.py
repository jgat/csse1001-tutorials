def find_numbers(text):
    result = []
    for word in text.split():
        if word.isdigit():
            result.append(int(word))
    return result

def find_numbers(text):
    return [int(word) for word in text.split() if word.isdigit()]

###############################################################################

def separate_comma(s): return s.split(',')
def separate_semicolon(s): return s.split(';')
def separate_pipe(s): return s.split('|')

def separate(delim):
    return lambda s: s.split(delim)

separate_comma = separate(',')
separate_semicolon = separate(';')
separate_pipe = separate('|')

###############################################################################

def simon_says():
    magic_word = "simon says "
    while True:
        cmd = raw_input("Command: ").lower()
        if cmd == 'q':
            break
        if cmd.startswith(magic_word):
            print "I will", cmd[len(magic_word):]
        else:
            print "I do nothing"


def get_commands():
    while True:
        cmd = raw_input("Command: ").lower()
        if cmd == 'q':
            break
        yield cmd


def simon_says2():
    magic_word = "simon says "
    for cmd in get_commands():
        if cmd.startswith(magic_word):
            print "I will", cmd[len(magic_word):]
        else:
            print "I do nothing"

###############################################################################

def permutations(xs):
    if len(xs) == 1:
        yield xs
    else:
        for i, x in enumerate(xs):
            for subperm in permutations(xs[:i]+xs[i+1:]):
                yield [x] + subperm
