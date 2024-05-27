# read foldernames from data/train

import os

def get_labels(path):
    if not os.path.exists(path):
        return []
    return os.listdir(path)

