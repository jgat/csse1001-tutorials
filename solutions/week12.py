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
    for x in items:
        d[x] = None
    return d.keys()

    ## This can be done in one line:
    # return dict.fromkeys(items).keys()

if __name__ == '__main__':
    #print uniqify([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
    #print uniqify2([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])
    #print uniqify3([8, 3, 5, 8, 9, 4, 2, 5, 3, 5])

    # Be aware: this can take 5-10 minutes to run.

    import random, timeit, math

    FUNCTIONS = [('uniqify3', 1000, lambda n: n),
                 ('uniqify2', 1000, lambda n: n * math.log(n, 2)),
                 ('uniqify', 1, lambda n: n ** 2)]
    for func, number, order in FUNCTIONS:
        print '\n' + func + ':'
        old = None
        for N in [1000, 2000, 4000, 8000, 16000, 32000, 64000]:
            time = min(timeit.repeat(func+'(range(N))', 'from __main__ import N,'+func, number=number))*1000/number
            print ('n = {:>5}: {:.4f} ms'.format(N, time) +
                   ('' if old is None else '   = {:.2f} times slower'.format(time/old)))
            old = time

        print "Extrapolating:"
        bigN = 10**6
        print "n = {:,>5}: {:.2f} seconds".format(bigN, time * order(bigN) / order(N) / 1000)
