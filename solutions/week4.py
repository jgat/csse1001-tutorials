# Note that iff is read as "if and only if".
def is_dna(string):
    """
    Returns True iff the input string is a valid DNA sequence.

    is_dna(str) -> bool
    """

    # -----------------------------------------------------------------------
    # For a string to be a dna sequence, it must be made up only of the
    # characters A, T, G, and C, and its length must be a multiple of 3. We
    # check each of these to determine whether any string is a dna sequence.
    #
    # We can only know that a string is a valid dna sequence after performing
    # each of these checks, whereas we can know it is invalid if it fails any
    # one of them, so we can only return True at the end (after all checks),
    # but we can return False early if we find that it is invalid. So a basic
    # template for our function could look like:
    #   Invalid length => return False
    #   Invalid character => return False
    #   return True
    #
    # First, check that the length of the string is a multiple of 3 (i.e.
    # dividing by 3 leaves no remainder)
    # -----------------------------------------------------------------------
    if len(string) % 3 != 0:
        # The length of this string is NOT a multiple of 3, so therefore this
        # string is not a dna sequence.
        return False
    
    # Iterate over each character in the string
    for char in string:
        # -------------------------------------------------------------------
        # Check that each character satisfies the requirements (i.e. is is
        # either A, T, G, or C, and nothing else).
        # -------------------------------------------------------------------
        
        # -------------------------------------------------------------------
        # A simple way to do this would be a nested if/elif/else:
        # if char == 'A':
        #     # Can't return True until we've checked ALL characters, so we 
        #     # just skip to the next one if this is a valid character.
        #     # Similarly below for T, G, & C.
        #     continue
        # elif char == 'T':
        #     continue
        # elif char == 'G':
        #     continue
        # elif char == 'C':
        #     continue
        # else:
        #     # Invalid dna character, so therefore this string is not a dna
        #     # sequence.
        #     return False
        
        # -------------------------------------------------------------------
        # While the above approach may see nice and easy, it is rather
        # tedious to write. What if we had to check for a combination of 10+
        # characters? That would be quite monotonous to write. Since we are
        # doing the same thing if the character is valid, we could use a
        # series of or operators. I.e.
        # if char == 'A' or char == 'T' or char == 'G' or char == 'C':
        #    continue
        # else:
        #    # Invalid dna character.
        #    return False
        # 
        # One could also achieve the same result by checking directly that
        # the current character is not invalid. I.e.
        # if char != 'A' and char != 'T' and char != 'G' and char != 'C':
        #     # Invalid dna character
        #     return False
        #
        # It is very important to note that a character is invalid if it is
        # not A and not T and not G and not C. If we were to check not A or
        # not T , etc., our condition would always evaluate to True, since at
        # least one of not A, not T, not G, not C is true for every single
        # character, and an or operator evaluates to True if at least one of
        # its operands are True.
        # -------------------------------------------------------------------

        # -------------------------------------------------------------------
        # Perhaps the easiest way to do this, by far, is to utilize the in
        # operator. This evaluates to True if the substring (or character,
        # since a character is a string of length 1) exists within the
        # string. We can use not to invert this test and check that the
        # character is not in the string of valid characters I.e.
        if char not in 'ATGC':
            return False
        # 
        # Or similarly with a list (although the above is easier to write):
        # if char not in ['A', 'T', 'G', 'C']:
        #   return False
        # -------------------------------------------------------------------

    # By now, we have performed every check for a valid dna sequence and
    # returned False if anything failed. Hence we only get to this line if
    # the string is not an invalid dna sequence, so therefore it must be
    # valid.
    return True

    # -----------------------------------------------------------------------
    # It should be noted that the checks can be performed in any order, it is
    # just usually easier to perform simpler checks before more complicated
    # ones. In this case, it is simpler to check the length of the string
    # than it is to iterate over each character and check if it is valid, but
    # performing that check first would still give a valid result.
    # -----------------------------------------------------------------------

def reverse_complement(dna):
    """
    Returns the reverse compliment of a dna sequence, or None if it is
    invalid.

    reverse_complement(str) -> str
    """

    # Ensure that the dna sequence is valid.
    if not is_dna(dna):
        # Return None for an invalid sequence
        return

    result = ''
    # For every character in the sequence, add its compliment to the result.
    for c in dna:
        if c == 'A':
            result += 'T'
        if c == 'T':
            result += 'A'
        if c == 'G':
            result += 'C'
        if c == 'C':
            result += 'G'

    # Return the reverse of the string
    return result[::-1]

# ---------------------------------------------------------------------------
# An alternate way of writing the body of this function would be to use a
# translation table.
# See string.maketrans
# from https://docs.python.org/2/library/string.html#string-functions
# We want to translate A   T   G   C
#                      |   |   |   |
#                     \_/ \_/ \_/ \_/
#                      T   A   C   G
# ---------------------------------------------------------------------------
# We need maketrans from the string library
from string import maketrans

# translation table
from_chars = 'ATGC'
to_chars   = 'TACG'
table = maketrans(from_chars, to_chars)
# This could be included in the function, but it is
# better to only have to build the translation table once and not rebuild it
# each time the function is called.

def reverse_complement(dna):
    """
    Returns the reverse compliment of a dna sequence, or None if it is
    invalid.

    reverse_complement(str) -> str
    """

    # Ensure that the dna sequence is valid.
    if not is_dna(dna):
        # Return None for an invalid sequence
        return

    # Translate each character and reverse the string.
    return dna.translate(table)[::-1] 

# ---------------------------------------------------------------------------

def print_codons(dna):
    """
    Prints the codons for a given dna sequence. Does nothing if the sequence
    is invalid.

    print_codons(str) -> None
    """

    # Do nothing if the dna sequence is not valid.
    if not is_dna(dna):
        return

    # Iterate over every third position in the string.
    for i in range(0, len(dna), 3):
        # Print this character and the following 2 (i.e. from i up to but not
        # including i + 3)
        print dna[i:i+3]

    # -----------------------------------------------------------------------
    # This can also be achieved using a while loop, as follows:
    # i = 0
    # while i < len(dna):
    #     print dna[i:i+3]
    #     i += 3
    # -----------------------------------------------------------------------


def get_number(string):
    """
    Returns the first non-negative integer in the string, or None if there
    are no integers in the string.

    Note that the question when states "positive integer", it is reasonable
    to include zero, so it really should state "non-negative integer".

    get_number(str) -> int
    """

    digits = ''
    # Iterate over every character in the string
    for char in string:
        if char.isdigit():
            # If the character is a digit, then append it to the result.
            digits += char
        elif digits:
            # If the character is not a digit, and we have found some digits
            # (i.e. digits != ''), then convert what we've found to an
            # integer.
            return int(digits)

    # Functions return None by default, so no return statement is necessary.
    # I.e. the following are redundant here:
    # return
    # return None


def get_number(string):
    """
    Returns the first integer in the string, or None if there are no
    integers in the string.

    get_number(str) -> int
    """
    # The buffer of digits to return.
    digits = ''
    # The previous character.
    prev = ''

    # Iterate over every character in the string
    for char in string:
        if char.isdigit():
            # If the character is a digit, then append it to the result.
            if prev '-':
                # If the previous character was -, begin digits with -.
                digits = '-'
            # Append this character to the digits buffer.
            digits += char
        elif digits:
            # If the character is not a digit, and we have found some digits
            # (i.e. digits != ''), then convert what we've found to an
            # integer.
            return int(digits)
            # Note that this case will not happen the first time we encounter
            # a minus sign if we've not previously encountered any digits,
            # since in this case the length of digits would be zero and
            # elif digits: would evaluate to False

        # Set the previous character to 
        prev = char

    # Functions return None by default, so no return statement is necessary.
    # I.e. the following are redundant here:
    # return
    # return None
