def sort(xs):
    if not xs:
        return xs
    m = min(xs)
    i = xs.index(m)
    return [m] + sort(xs[:i] + xs[i+1:])

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
