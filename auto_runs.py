'''Run the solver against all words of the dictionnary and evaluates performances.'''

import numpy as np
import shortlist as st
import game as ga
import tools as tl
import os
import time as t

dir_path = os.path.dirname(os.path.realpath(__file__))

if 'words_ranked.txt' not in os.listdir(dir_path):
    tl.write_1st_guess()    

continuous_scoring = False

short_list = st.Shortlist()
short_list.read_1st_guess()

number_words = len(short_list.words)
number_iterations = []
population_per_number_iteration = 20*[0]
time_per_guess = []

for secret_word in short_list.words:
    wordle = ga.Wordle()
    wordle.word = secret_word
    short_list.reset_all_temp()
    algo_word = short_list.best_guess()
    iter = 0
    while algo_word != secret_word:
        output = wordle.evaluate_guess(algo_word)
        tempo = t.time()
        short_list.shorting_from_output(algo_word,output)
        time_per_guess.append(t.time()-tempo)
        if len(short_list.temp_words)>0 and continuous_scoring == True:
            short_list.update_scoring() 
        algo_word = short_list.best_guess()
        iter+=1
    number_iterations.append(iter)
    population_per_number_iteration[iter]+=1

print('Average number of guesses :', np.mean(number_iterations))

# 3.98 vs 4.00 for continuous scoring

print('Number of words for each performance :')
print('Guesses to solve | % Words  | Cumulated %')
s=0
for i, el in enumerate(population_per_number_iteration):
    s+=el
    print('       ',i, '         ', '{:.2f}'.format(100*el/number_words), '      ', '{:.2f}'.format(100*s/number_words))

# 91.75% of the words are discovered in 6 guesses.

print('Average time per guess :', '{:.5f}'.format(np.mean(time_per_guess)),' seconds.')

# 5e-4 seconds.


'''Yoann Launay, University of Cambridge, 12/22.'''