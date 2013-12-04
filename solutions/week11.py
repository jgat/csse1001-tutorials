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
