def read_scores(filename):
    """
    Returns a dictionary of scrabble scores from the given file, with each
    letter as the key and the corresponding score as the value.

    read_scores(str) -> dict(str: int)
    """
    fd = open(filename, 'rU')
    scores = {}

    for line in fd:
        letter, score = line.split(',')
        scores[letter] = int(score)
    return scores

    # -----------------------------------------------------------------------
    # As an aside, this function can also be implemented using dictionary
    # comprehension (similar to list comprehension, which will be introduced
    # later in the course). Note that this is included as an aside for
    # students who may find it interesting.
    # with open(filename, 'rU') as fd:
    #     return dict((line[0], line[1]) for line in fd)
    # -----------------------------------------------------------------------

# ---------------------------------------------------------------------------
# The reason why we can't write a dictionary which does the reverse, that is,
# maps a scrabble score to the letter it corresponds to is that scores are
# not necessarily unique (i.e. multiple letters could have the same score).
# A dictionary's keys are unique, so therefore a scrabble score could not be
# a key.
#
# Note that we could however have a dictionary with scores as keys if the 
# corresponding values were a list of letters that corresponded to the score.
# ---------------------------------------------------------------------------

def get_score(scores, word):
    """
    Returns the scrabble score for the given word.

    get_score(dict(str: int), str) -> int
    """

    # Start with no score.
    score = 0

    # For each letter in the word, add the score for that letter to the total
    # score.
    for letter in word:
        score += SCORES[letter]

    return score


# Load the scores from the score file
# Note that all capitals represents a constant (i.e. the value is not
# intended to change).
SCORES = read_scores('../tasks/scrabble_scores.txt')

import pprint
pprint.pprint(SCORES)

print get_score('quack')

#############################################################################

def read_config(filename):
    """
    Returns a dictionary representation of the configuration data in the
    given file.

    read_config(str) -> dict(str: dict(str: str))
    """

    fd = open(filename, 'rU')

    # Resulting configuration dictionary
    config = {}

    # Store the current heading (i.e. the last one encountered)
    heading = None

    # Iterate over each line in the file.
    for line in fd:
        # First strip the line of surrounding whitespace.
        line = line.strip()

        if line.startswith('[') and line.endswith(']'):
            # If the line is wrapped with square brackets, it is a major key.

            # The heading does not include [ or ]
            heading = line[1:-1]

            # Create a new dictionary for the settings under this heading.
            config[heading] = {}

        elif line.count('=') == 1 and heading is not None:
            # Else if this line contains equals and we've seen a heading.

            # Get the name and value from this line.
            name, value = line.split('=')

            # Set the appropriate key/value in the configuration dictionary
            # for the current heading.
            config[heading][name.strip()] = value.strip()

        else:
            # If the config file is invalid, raise a ValueError.
            raise ValueError('Invalid config file.')

    fd.close()

    return config



config = read_config('../tasks/config.txt')

def get_value(config, name):
    """
    Returns the setting name from the configuration dictionary.

    get_value(dict(str: dict(str: str)), str) -> str
    """
    # Split the name of the setting over the fullstop.
    a, b = name.split('.')

    # Return the appropriate value.
    return config[a][b]

print get_value(config, 'user.mobile')
print get_value(config, 'notifications.email')