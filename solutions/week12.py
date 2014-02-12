def uniqify(items):
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result

def uniqify2(items):
    result = []
    for x in sorted(items):
        if result == [] or x != result[-1]:
            result.append(x)
    return result

def uniqify3(items):
    return dict.fromkeys(items).keys()

#print uniqify([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
#print uniqify2([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
#print uniqify3([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])

import random
import timeit

# TODO: work in progress - calibrate parameters

def test(function_name, size, repeat, number):
    stmt = "{0}(xrange({1}))".format(function_name, size)
    setup = "from __main__ import {0}".format(function_name)
    return min(timeit.repeat(stmt, setup, repeat=repeat, number=number)) / number

print test('uniqify', 5000, 10, 1)
print test('uniqify', 10000, 10, 1)
print test('uniqify', 20000, 10, 1)

print test('uniqify2', 50000, 10, 1)
print test('uniqify2', 100000, 10, 1)
print test('uniqify2', 200000, 10, 1)

print test('uniqify3', 50000, 10, 1)
print test('uniqify3', 100000, 10, 1)
print test('uniqify3', 200000, 10, 1)
