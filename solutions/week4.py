def is_dna(string):
    for c in string:
        if c not in 'ACTG':
            return False
    return len(string) % 3 == 0


def reverse_complement(dna):
    if not is_dna(dna):
        return
    result = ''
    for c in dna:
        if c == 'A':
            result += 'T'
        if c == 'T':
            result += 'A'
        if c == 'G':
            result += 'C'
        if c == 'C':
            result += 'G'
    return result[::-1]


def print_codons(dna):
    if not is_dna(dna):
        return
    i = 0
    while i < len(dna):
        print dna[i:i+3]
        i += 3


def get_number(string):
    digits = ''
    for c in string:
        if c.isdigit():
            digits += c
        elif digits:
            return int(digits)


def get_number(string):
    digits = ''
    prev = ''
    for c in string:
        if c.isdigit():
            if prev == '-':
                digits += '-'
            digits += c
        elif digits:
            return int(digits)
        prev = c
