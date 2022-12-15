'''auto play many times'''

import numpy as np
import shortlist as st

continuous_scoring = False

ini_short_list = st.Shortlist()
ini_short_list.read_1st_guess()
word_ini = ini_short_list.best_guess(print_= True)

number_words = len(ini_short_list.words)

for i, secret_word in enumerate(ini_short_list.words):
    algo_word = word_ini
    temp_short_list = st.Shortlist
    while algo_word != secret_word:
        #so

while input_user_choice != '':
    input_user_response = input('What is the answer of Wordle ? Enter a string of length 5 (- for grey, g for green, y for yellow)')
    short_list.shorting_from_output(input_user_choice,input_user_response)
    if len(short_list.temp_words)>0 and continuous_scoring == True:
        short_list.update_scoring() 
    short_list.print_top() 
    input_user_choice = input('What is your chosen guess? (Press enter to exit)')
