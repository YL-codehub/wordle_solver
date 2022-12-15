'''auto play many times'''

import numpy as np
import shortlist as st
import game as ga

continuous_scoring = False

short_list = st.Shortlist()
short_list.read_1st_guess()

number_words = len(short_list.words)
number_iterations = []

for i, secret_word in enumerate(short_list.words):
    wordle = ga.Wordle()
    wordle.word = secret_word
    short_list.reset_all_temp()
    algo_word = short_list.best_guess() # probably 'aeros'
    iter = 0
    # print('------------------')
    # print('secret word : ',secret_word)
    # print('------------------')
    while algo_word != secret_word:
        output = wordle.evaluate_guess(algo_word)
        # print(algo_word,output)
        short_list.shorting_from_output(algo_word,output)
        algo_word = short_list.best_guess()
        iter+=1
    number_iterations.append(iter)
    # if i>1000:
    #     break

print('Average number of guesses :', np.mean(number_iterations))
print('Maximum number of iterations :', np.max(number_iterations))
