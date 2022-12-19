'''
Wordle is implemented in this class and returns the same outputs as online ones.
Having a local version is useful to avoid the use of an API or an extra-package to get faster input/outputs than the human/main.py interface.
'''

# The game is an object
class Wordle:
    """ Class imitating WordleGame.org © 2022 input and outputs."""
    def __init__(self):
        self.word = None

    def evaluate_guess(self, word, print_ = False):
        '''str ---> str 
        From a word of 5 letters (in the dictionnary or not), returns the Wordle comparison to the secret word (stored in self.word).
        '-', equivalent to grey, indicates that the letter isn't in the target word at all.
        'y', equivalent to yellow, indicates that the letter is in the word but in the wrong spot.
        'g', equivalent to green, indicates that the letter is in the word and in the correct spot.
        The return can be print in the terminal if print_ = True.'''

        # Stop evuluating if successful guess
        if word == self.word:
            if print_:
                print('Success!')
            return 'ggggg'

        else:
            word_split = list(word)
            answer = ''

            # Different method if two identical letters in the input
            # Note that there is no 5-word with 3 identical letters.
            assigned_double_letters = []       

            # Each input letter is scanned from left to right
            for i,letter in enumerate(word_split):
                # Dichotomy structure
                if letter in self.word:
                    # Need to test the rest of the input word for identical letter inputs 
                    word_elsewhere = word_split[:i]+word_split[i+1:]
                    # Immediate green case
                    if self.word[i] == letter:
                        answer += 'g'
                    else:
                        # Immediate yellow if single letter input
                        if not(letter in word_elsewhere): #ie if you give twice the same letter
                            answer += 'y'
                        # If not, impossible to assign colors independently 
                        else:
                            # Case where the same letter is given twice but is not twice in the secret word
                            if self.word.count(letter)< word.count(letter):
                                # If the letter has already been searched for, the single 'y' allowed has already been used.
                                if letter in assigned_double_letters:
                                    answer += '-'
                                # Otherwise, need to assign and record the assignment
                                else:
                                    # Need to scan secret word but not where double letters are
                                    word_out_letters = [self.word[i] for i in range(5) if word[i]!= letter ] #remove self.word indices corresponging to my double letters
                                    # Case where the letter is not at any of both input spots 
                                    if letter in word_out_letters:
                                        answer += 'y'
                                    # Otherwise the other letter is green
                                    else: 
                                        answer +='-'
                                    assigned_double_letters.append(letter)
                            else:
                                answer += 'y'
                # Immediate grey case
                else:
                    answer+='-'
            if print_:
                print(answer)
            return answer


# unit tests
# wordle = Wordle()

# wordle.word = 'rally'
# print(wordle.evaluate_guess('aeros'))
# print(wordle.evaluate_guess('riata'))
# print(wordle.evaluate_guess('rainy'))
# print(wordle.evaluate_guess('rally'))

# wordle.word = 'share'
# print(wordle.evaluate_guess('aeros'))
# print(wordle.evaluate_guess('erase'))
# print(wordle.evaluate_guess('spare'))
# print(wordle.evaluate_guess('share'))

# wordle.word = 'vomit'
# print(wordle.evaluate_guess('aeros'))
# print(wordle.evaluate_guess('noily'))
# print(wordle.evaluate_guess('comic'))
# print(wordle.evaluate_guess('vomit'))

# wordle.word = 'voter'
# print(wordle.evaluate_guess('aeros'))
# print(wordle.evaluate_guess('camel'))
# print(wordle.evaluate_guess('tight'))
# print(wordle.evaluate_guess('comic'))
# print(wordle.evaluate_guess('forte'))
# print(wordle.evaluate_guess('magic'))


#### answers 

# # y-y--
# # g-y--
# # gg--g
# # ggggg
# # yyy-y
# # -ygyg
# # g-ggg
# # ggggg
# # ---y-
# # -gy--
# # -ggg-
# # ---y-
# # -gy--
# # -ggg-
# # ggggg
# # -yyy-
# # ---g-
# # y----
# # -g---
# # -gyyy
# # -----

'''Yoann Launay, University of Cambridge, 12/22.'''