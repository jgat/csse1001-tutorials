def uniquify(items):
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result

def uniquify2(items):
    result = []
    for x in sorted(items):
        if result == [] or x != result[-1]:
            result.append(x)
    return result

def uniquify3(items):
    return dict.fromkeys(items).keys()

#print uniquify([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
#print uniquify2([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
#print uniquify3([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])

import random
import timeit

N = 100000
items = [random.randint(0,N) for i in xrange(N)]
print "uniquify3:", min(timeit.repeat('uniquify3(items)', 'from __main__ import uniquify3, items', number=100))/100, 'seconds'
print "uniquify2:", min(timeit.repeat('uniquify2(items)', 'from __main__ import uniquify2, items', number=100))/100, 'seconds'
print "uniquify:", min(timeit.repeat('uniquify(items)', 'from __main__ import uniquify, items', number=1)), 'seconds'
