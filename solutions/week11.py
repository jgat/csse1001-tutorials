def minimum(xs):
    """
    Our task is to write a recursive method to solve this problem.

    Recursion is about continually reducing a problem by a small step until we
    reach a base case - that is, a case where the result is trivial
    (requires little to no calculation)

    Firstly, we assume that a list must be non-empty. With this in mind, the 
    simplest case we could have is a list with a single element, where the
    minimum element is simply the first and only element in the list.

    Now to write this method recursively, we need to determine the relation
    between a more complex case (i.e. a list with 2 or more elements). We should
    assume that our method will work correctly for a simpler case, and use that
    to build up to a larger case.

    Consider the list:
        xs = [5, 4, -2, 3, 10]

    We could notice that if we select the first element, 5, that it is possible 
    for it to be only the minimum element if it is <= than the minimum element
    of the sub list containing all the other elements (i.e. [4, -2, 3, 10])

    This would give a generalization that the minimum of xs is
        min(5, minimum([4, 3, .., 10]))
        (with min returning the lowest value of all its arguments; i.e.
        min(3, -5) => -5; type help(min) for more info)

    And minimum([4,3, ..,10])) would similarly be equivalent to
        min(4, [3, .., 10])

    And so we can see that we could achieve this method recursively, because
    here 5 is the first element, so in every non-base case, we would have
        minimum(xs) == min(xs[0], minimum(xs[1:])
        (with xs[0] being the first element, and xs[1:] being the rest)

    And we know that the case of minimum(xs[1:]) is simpler than minimum(xs)
    because xs[1:] is a smaller list than xs (it has one less element), so we
    will eventually reach the base case.

    So therefore our code becomes:
    """
    # In the case of an empty list, we will raise an error
    # Equivalent checks are:
    # if not len(xs):   # Check that the length is not non-zero
    # if not xs: # Check that the list does not contain anything
    if len(xs) == 0:
        raise ValueError("Empty list does not have a smallest element.")
    if len(xs) == 1:
        # Base case
        # If a list has one element, this is the smallest element in the list
        return xs[0]
    else:
        # Non-trivial case
        # minimum(xs) == min(xs[0], minimum(xs[1:])); which approaches base case
        return min(xs[0], minimum(xs[1:]))

    """
    We could also note that the minimum element of our list must be the lesser
    value of the minimum of any two sub lists. This could lead to a similar
    implementation of the non-trivial case:

    middle = len(xs)/2
    minimum(xs) == min(minimum(xs[0:middle]), minimum(xs[middle:]))
    """

###############################################################################

import os

def list_files(directory):
    # A list to hold paths to every file in directory and its subdirectories.
    all_files = []
    # Iterate over every entry in this directory (files and subdirectories)
    for filename in os.listdir(directory):
        # Get the full path of the file/subdirectory, by prefixing directory
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            # If the current filepath points to a directory, we need to repeat
            # the process on that subdirectory and add each item from the
            # resulting list to ours. list.extend allows us to do so
            all_files.extend(list_files(filepath))
        else:
            # If the current filepath points to a file, just add it to the list
            all_files.append(filepath)
    # Return the list of all files at the end
    return all_files

if __name__ == '__main__':
    # Raises AssertionError iff (if and only if) expression is equivalent to
    # False (i.e. bool(expression) is False); otherwise does nothing.
    assert minimum([2, 5, 1, 3, 4, 2]) == 1
    print list_files('..')
