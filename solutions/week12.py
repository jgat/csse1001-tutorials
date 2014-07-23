def uniqify(items):
    # -------------------------------------------------------------------------
    # In order to return a new list with all elements of item occurring at most
    # once (i.e. duplicates removed), we need to start with an empty result
    # list iterate over every element, check if it already exists in the result
    # list, and if not add it to the result list.
    # -------------------------------------------------------------------------
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result

    # -------------------------------------------------------------------------
    # The complexity of this function is quadratic. It may seem to be linear at
    # first, in that we only iterate over the initial list one level deep, but
    # it is actually quadratic, because to check if an element is in our result
    # list, we must also iterate over that (hence we have a loop two levels
    # deep).
    # 
    # The size of result will approach the size of items, and in the worst case
    # scenario, when items is unique, it will end up having the same size as
    # items, so it is clearly quadratic.
    # -------------------------------------------------------------------------


def uniqify2(items):
    # -------------------------------------------------------------------------
    # If we start with a sorted list, we know that duplicates will be
    # consecutive, and hence as we iterate over the list to consider whether or
    # not to add them to our result list, we will be considering them
    # consecutively. We will be adding a duplicate therefore, if the previously
    # added element is the same as that which we are currently considering.
    # This is because the data is sorted.
    # 
    # So if the current list element is the same as the last element in the
    # result list, we should ignore this element. We need to also ensure that
    # there is at least one element in the result list, otherwise trying to
    # retrieve the last element will raise an error. This means that we need to
    # use an "and".
    # -------------------------------------------------------------------------
    result = []
    for x in sorted(items):
        # the same as:
        # if len(result) != 0 and result[-1] == x:
        # or
        # if result != [] and result[-1] == x:
        if len(result) and result[-1] == x:
            # skip over this item
            continue
        # otherwise, append it to the result list
        result.append(x)
    return result

    # -------------------------------------------------------------------------
    # Alternatively, we could consider the inverse case, such that we only want
    # to add items if they do not match the last item in result. The special
    # case here is that we also want to add items if the result list is empty
    # (i.e. it has no elements to compare against). We want to add the item
    # currently being considered in either of these cases (i.e. we need to use
    # "or") leading us to the following.
    # -------------------------------------------------------------------------
    
    """
    result = []
    for x in sorted(items):
        # the same as:
        # if result == [] or x != result[-1]:
        # or
        # if not len(result) or x != result[-1]:
        if not result or x != result[-1]:
            # append this item to the list
            result.append(x)
    return result
    """

    # -------------------------------------------------------------------------
    # Regarding the time complexity of this solution, the loop itself is
    # linear, in that the supplied list is iterated over once, and in a loop
    # one level deep. However, the initial sorting of the list (using sorted),
    # is of complexity n log(n), which means that the overall time complexity
    # of this function is n log(n).
    # -------------------------------------------------------------------------


def uniqify3(items):
    # -------------------------------------------------------------------------
    # The data type that we have encountered with a notion of uniqueness is a
    # dictionary, which has unique keys mapping to values (which are not
    # necessarily unique; i.e. a dictionary could have two keys mapping to the
    # same value, but cannot have the same key mapping to two different
    # values).
    # 
    # So instead of using a result list, we could use a result dictionary. We
    # can blindly add each item in items to the result dictionary since if we
    # add a duplicate it will just overwrite the other matching key with the
    # same. Then we can just extract the keys into a result list, and we're
    # done.
    # -------------------------------------------------------------------------

    result_dict = {}
    for x in items:
        result_dict[x] = x  # or some abitrary value
                            # the only important part here is:
                            # result_dict[x] = ...

    result_list = []
    for x in result_dict.keys():
        result_list.append(x)

    return result_list

    # -------------------------------------------------------------------------
    # The astute student will note that result_dict.keys() returns a list of
    # keys, so we could simplify the above to:
    # return result_dict.keys()
    # 
    # We could actually simplify this entire solution into one line (although
    # this makes the complexity harder to determine), by utilizing the fromkeys
    # method of the dict class. Type help(dict.fromkeys) for more information.
    # -------------------------------------------------------------------------
    return dict.fromkeys(items).keys()

    # -------------------------------------------------------------------------
    # As far as complexity goes, it is easy to see from the expanded solution
    # above that we have two loops that are each one level deep (i.e. no nested
    # loops). This means that our function is linear in complexity. Similarly,
    # the more one-liner above is functioning in the same manner, so it is also
    # linear in complexity. It is worth nothing that the above relies upon the
    # average time for list.append being constant, and the average time for
    # dict.keys being linear (which is the case).
    # 
    # Furthermore, it is impossible to solve this question with a faster time
    # complexity than in this function (uniqify3), since we must consider each
    # element in items at least once (which is linear in nature), so in the
    # very least, our complexity must be linear. Therefore it cannot have a
    # better time complexity than this.
    # -------------------------------------------------------------------------

##################################################
################### Time Tests ###################
##################################################

if __name__ == '__main__':
    # -----------------------------------------------------------------------------
    # Notice the difference between each version of uniqify, and that it increases
    # significantly with each power of 10.
    # 
    # Note also that uniqify will take a considerable amount of time to complete
    # for 64000 items.
    # 
    # This demonstrates the significance of time complexity.
    # -----------------------------------------------------------------------------
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

