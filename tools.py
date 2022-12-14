import numpy as np
def split_in_array(words):
    words_split = []
    for string in words:
        words_split.append(list(string))
    return np.array(words_split)