'''Secondary functions, mainly for scoring.'''
import numpy as np

def split_in_array(words):
    '''list of str ---> 2D np.array of chars
    In a list, splits words into the list of their separated letters.'''
    words_split = []
    for string in words:
        words_split.append(list(string))
    return np.array(words_split)

def letters_score(words_split):
    '''2D np.array of chars ---> list of floats
    Scores each letter depending on the probability to find them in the 5-words dictionnary.
    Result stored in a list, the indices of which are the chr codes of the letters (eg 0 is 'a').'''
    score_letters =[]
    for i in range(97,123):
        score_letters.append(np.sum(words_split == chr(i))) #counting the occurences for each letter
    score_letters = 1/(score_letters/np.sum(score_letters)) #the less the better
    return score_letters

def alphabet_scorer(letter, score_letters):
    '''(char, list) ---> float
    Evaluates previous score vector directly from the char.'''
    return score_letters[ord(letter)-97]

# Vectorizing previous function for quick scoring of an array of letters
vec_alphabet_scorer = np.vectorize(alphabet_scorer, excluded={1})

def diversity_scorer(word): 
    '''str ---> float
    Returns the number of unique letters in an input word.'''
    return len(set(word))

# Vectorizing previous function for quick scoring of an array of words
vec_diversity_scorer = np.vectorize(diversity_scorer)

def word_scorer(words, words_split, diversity = True):
    '''(list of str, np.arr of char) ---> np.array of float
    Returns the scores' list of words in a list.
    The score is proportional to the score of its letters and inverse-proportional its diversity:
    the smallest = the better in our metric.'''
    score_letters = letters_score(words_split)
    d = 1
    if diversity:
        d = vec_diversity_scorer(words)
    return np.sum(vec_alphabet_scorer(words_split,score_letters),axis=1)/d 

def rank_words(words,words_split):
    '''(list of str, np.arr of char) ---> (np.array of str, np.array of chr, np.array of float)
    Uses word_scorer to rank words and their splits.
    Returns them from best guess to worst, i.e. lowest score to highest.'''
    scores = word_scorer(words,words_split)
    scores_arg_sort = np.argsort(scores)
    return words[scores_arg_sort], words_split[scores_arg_sort], scores[scores_arg_sort]

def write_1st_guess():
    '''Calculates the ranking from 'words.txt', given rank_words function and writes it in the 'words_ranked.txt' file for later use.'''
    words = np.loadtxt('words.txt',dtype='str')
    words_split = split_in_array(words)
    words, words_split, scores = rank_words(words, words_split)
    to_be_written = np.hstack((np.array([words]).T,np.array([scores]).T))
    np.savetxt('words_ranked.txt', to_be_written, fmt = '%s') #but should rather choose words with different letters


'''Yoann Launay, University of Cambridge, 12/22.'''
