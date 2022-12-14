'''Infinite loop while interface.'''
import numpy as np
import shortlist as st

short_list = st.Shortlist()
short_list.read_1st_guess()
short_list.print_top()
# short_list.print_best()


# test 1 'dylde'
# short_list.shorting_from_output('aeros','--y--')
# short_list.print_top() 
# short_list.shorting_from_output('trilde','-g-gy')
# short_list.print_top() 

#test 2 'money'
# short_list.shorting_from_output('serai','-y---')
# short_list.print_top() 
# short_list.shorting_from_output('olent','y-yy-')
# short_list.print_top() 
# short_list.shorting_from_output('donee','-ggg-')
# short_list.print_top() 

#test 3 'guava'
# short_list.shorting_from_output('aeros','y----')
# short_list.print_top() 
# short_list.shorting_from_output('dital','---y-')
# short_list.print_top() 
# short_list.shorting_from_output('yamun','-y-y-')
# short_list.print_top() 
# short_list.shorting_from_output('pucka','-g--g')
# short_list.print_top() 
# short_list.shorting_from_output('buffa','-g--g')
# short_list.print_top() 
# short_list.shorting_from_output('huzza','-g--g')
# short_list.print_top() 



input_user_choice = input('What is your first guess choice?')
while input_user_choice != '':
    input_user_response = input('What is the answer of Wordle ? Enter a string of length 5 (- for grey, g for green, y for yellow)')
    short_list.shorting_from_output(input_user_choice,input_user_response)
    short_list.print_top() 
    input_user_choice = input('What is your chosen guess? (Press enter to exit)')