'''Infinite loop while interface.'''
import numpy as np
import shortlist as st
import tools as tl
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

if 'words_ranked.txt' not in os.listdir(dir_path):
    tl.write_1st_guess()    

continuous_scoring = True

short_list = st.Shortlist()
short_list.read_1st_guess()
short_list.print_top()

input_user_choice = input('What is your first guess choice?')
while input_user_choice != '':
    input_user_response = input('What is the answer of Wordle ? Enter a string of length 5 (- for grey, g for green, y for yellow)')
    short_list.shorting_from_output(input_user_choice,input_user_response)
    if len(short_list.temp_words)>0 and continuous_scoring == True:
        short_list.update_scoring() 
    short_list.print_top() 
    input_user_choice = input('What is your chosen guess? (Press enter to exit)')


'''Yoann Launay, University of Cambridge, 12/22.'''
