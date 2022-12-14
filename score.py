'''Independent scoring'''
#make a function of it in tools? and save in file as option?
# function of the words split...
import numpy as np
import tools as tl

words = np.loadtxt('words.txt',dtype='str')
words_split = tl.split_in_array(words)

score_letters =[]
for i in range(97,123):
    score_letters.append(np.sum(words_split == chr(i))) #counting the occurences for each letter

score_letters = 1/(score_letters/np.sum(score_letters)) #the less the better

def alphabet_scorer(letter):
    return score_letters[ord(letter)-97]

vec_alphabet_scorer = np.vectorize(alphabet_scorer) #wrapper for fast scoring

def diversity_scorer(word): # Maybe later...
    return len(set(word))

vec_diversity_scorer = np.vectorize(diversity_scorer)
# print(words[0:10])
# print(vec_diversity_scorer(words[0:10]))

def word_scorer(arr, Diversity = 1):
    return np.sum(vec_alphabet_scorer(arr),axis=1)/Diversity 

scores_word = word_scorer(words_split,Diversity=vec_diversity_scorer(words))

scores_arg_sort = np.argsort(scores_word)
ranked_words = words[scores_arg_sort]


to_be_written = np.hstack((np.array([ranked_words]).T,np.array([scores_word[scores_arg_sort]]).T))
np.savetxt('words_ranked.txt', to_be_written, fmt = '%s') 

