def read_scores(filename):
    fd = open(filename, 'rU')
    scores = {}
    for line in fd:
        letter, score = line.split(',')
        scores[letter] = int(score)
    return scores

SCORES = read_scores('../tasks/scrabble_scores.txt')

import pprint
pprint.pprint(SCORES)


def get_score(word):
    score = 0
    for letter in word:
        score += SCORES[letter]
    return score

print get_score('quack')

###############################################################################


def read_config(filename):
    fd = open(filename, 'rU')
    config = {}
    heading = None
    for line in fd:
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            heading = line[1:-1]
            config[heading] = {}
        elif line.count('=') == 1 and heading is not None:
            name, value = line.split('=')
            config[heading][name] = value
        else:
            raise ValueError('invalid config file')
    return config

config = read_config('../tasks/config.txt')
pprint.pprint(config)


def get_value(config, name):
    a, b = name.split('.')
    return config[a][b]

print get_value(config, 'user.mobile')
print get_value(config, 'notifications.email')
