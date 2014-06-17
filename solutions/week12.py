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
    d = {}
    for x in xs:
        d[x] = None
    return d.keys()

    ## This can be done in one line:
    # return dict.fromkeys(items).keys()


if __name__ == '__main__':
    #print uniqify([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
    #print uniqify2([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
    #print uniqify3([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])

    # Run this at the beginning of the tutorial hour.
    # The N = 10**6 case will not finish in time

    import random
    import timeit

    for N in [1000, 10000, 100000, 1000000]:
        items = [random.randint(0,N) for i in xrange(N)]
        print "n =", N
        print "uniqify3:", min(timeit.repeat('uniqify3(items)', 'from __main__ import uniqify3, items', number=100))/100, 'seconds'
        print "uniqify2:", min(timeit.repeat('uniqify2(items)', 'from __main__ import uniqify2, items', number=100))/100, 'seconds'
        print "uniqify:", min(timeit.repeat('uniqify(items)', 'from __main__ import uniqify, items', number=1)), 'seconds'
        print

