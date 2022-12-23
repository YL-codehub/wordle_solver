'''Run the solver against all words of the 5-words dictionnary and evaluates performances.'''

# Packages and libraries
import numpy as np
import shortlist as st
import game as ga
import tools as tl
import os
import time as t

# Profilers, turn it on/off depending on your needs
line_profiling = False
memory_profiling = False

# Line profiling starts if True
if line_profiling:
    from pyinstrument import Profiler
    profiler = Profiler(interval=0.00001)
    profiler.start()

# Checking if initial ranking has been done
dir_path = os.path.dirname(os.path.realpath(__file__))
if 'words_ranked.txt' not in os.listdir(dir_path):
    tl.write_1st_guess()    

# Scoring at each guess or not
continuous_scoring = False

# Initialization
short_list = st.Shortlist()
short_list.read_1st_guess()

number_words = len(short_list.words)
number_iterations = []
population_per_number_iteration = 17*[0]
time_per_guess = []

# Test solver for each word of the dictionnary
for secret_word in short_list.words:
    wordle = ga.Wordle()
    wordle.word = secret_word
    short_list.reset_all_temp()
    algo_word = short_list.best_guess()
    iter = 0
    # Ask for guesses until solver succeeds 
    while algo_word != secret_word:
        
        # use local implementation of wordle to evaluate the guess
        output = wordle.evaluate_guess(algo_word)
        tempo = t.time()
        
        # update the solver's shortlist given Wordle's hints output
        short_list.shorting_from_output(algo_word,output)
        time_per_guess.append(t.time()-tempo)

        # if continous scoring, update the scoring
        if len(short_list.temp_words)>0 and continuous_scoring == True:
            short_list.update_scoring() 
        
        # increment analytics
        algo_word = short_list.best_guess()
        iter+=1
        if iter>16:
            raise ValueError("Number of max necessary guesses is more than v0's.")
    number_iterations.append(iter)
    population_per_number_iteration[iter]+=1

print('--------------------------------------------------------------')
if line_profiling:
    profiler.stop()
    print('Line profiling:')
    profiler.print()
    print('--------------------------------------------------------------')

if memory_profiling:
    from pympler import summary, muppy
    print('Memory profiling:')
    allObjects = muppy.get_objects()
    sum = summary.summarize(allObjects)
    summary.print_(sum)
    print('--------------------------------------------------------------')

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

# 5e-4 seconds vs more for continuous scoring.

'''Yoann Launay, University of Cambridge, 12/22.'''