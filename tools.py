import numpy as np

def split_in_array(words):
    words_split = []
    for string in words:
        words_split.append(list(string))
    return np.array(words_split)

def letters_score(words_split):
    score_letters =[]
    for i in range(97,123):
        score_letters.append(np.sum(words_split == chr(i))) #counting the occurences for each letter
    score_letters = 1/(score_letters/np.sum(score_letters)) #the less the better
    return score_letters

def alphabet_scorer(letter, score_letters):
    return score_letters[ord(letter)-97]

vec_alphabet_scorer = np.vectorize(alphabet_scorer, excluded={1}) #wrapper for fast scoring, for 1st argument only!

def diversity_scorer(word): 
    return len(set(word))

vec_diversity_scorer = np.vectorize(diversity_scorer)

def word_scorer(words, words_split, diversity = True):
    score_letters = letters_score(words_split)
    d = 1
    if diversity:
        d = vec_diversity_scorer(words)
    return np.sum(vec_alphabet_scorer(words_split,score_letters),axis=1)/d 

def rank_words(words,words_split):
    scores = word_scorer(words,words_split)
    scores_arg_sort = np.argsort(scores)
    return words[scores_arg_sort], words_split[scores_arg_sort], scores[scores_arg_sort]

# words = np.loadtxt('words.txt',dtype='str')
# words_split = split_in_array(words)
# print(letters_score(words_split))
# print(vec_alphabet_scorer(np.array([['a','b','c'],['d','e','f']]),letters_score(words_split)))
# print(rank_words(words,words_split)[0:10])


# to_be_written = np.hstack((np.array([ranked_words]).T,np.array([scores_word[scores_arg_sort]]).T))
# np.savetxt('words_ranked.txt', to_be_written, fmt = '%s') #but should rather choose words with different letters