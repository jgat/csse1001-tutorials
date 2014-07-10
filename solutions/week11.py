# Three different solutions are presented

def minimum(xs):
    if not xs:
        raise ValueError("Empty list does not have a smallest element.")
    if len(xs) == 1:
        return xs[0]
    else:
        return min(xs[0], minimum(xs[1:]))


def minimum(xs):
    if not xs: raise ValueError()
    if len(xs) == 1: return xs[0]

    # len(xs) >= 2
    if xs[0] > xs[1]:
        return minimum(xs[:1] + xs[2:])
    else:
        return minimum(xs[1:])


def minimum(xs):
    # Note - the depth of the recursion tree is logarithmic, but the complexity
    #        is still linear in the length of the list.
    if not xs: raise ValueError()
    if len(xs) == 1: return xs[0]

    # len(xs) >= 2  ensures that  xs[:mid] != [] and xs[mid:] != []
    mid = len(xs) / 2
    return min( minimum(xs[:mid]), minimum(xs[mid:]) )


###############################################################################

import os


def list_files(directory):
    all_files = []
    for filename in os.listdir(directory):
        full_name = os.path.join(directory, filename)
        if os.path.isdir(full_name):
            all_files.extend(list_files(full_name))
        else:
            all_files.append(full_name)
    return all_files

if __name__ == '__main__':
    import pprint
    assert minimum([2, 5, 1, 3, 4, 2]) == 1
    pprint.pprint(list_files('..'))
