# show subfolders from data folder

import os

def show_subfolders(path):
    arr = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            arr.append(name)
    return arr

print(show_subfolders('data'))

