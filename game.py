'''
Wordle is implemented in this class and returns the same outputs as online ones.
Having a local version is useful to avoid the use of an API or an extra-package to get faster input/outputs than the human-main.py interface.
'''

class Wordle:
    """ Class maintening remaining possibilities  """
    def __init__(self):
        self.word = None

    def random_draw(self):
        return True

    def evaluate_guess(self, word, print_ = False):
        if word == self.word:
            if print_:
                print('Success!')
            return 'ggggg'
        else:
            word_split = list(word)
            answer = ''
            assigned_double_letters = [] #different management if two letters as an input # there's no 5-word with 3 identical letters       
            for i,letter in enumerate(word_split):
                if letter in self.word:
                    word_elsewhere = word_split[:i]+word_split[i+1:]
                    if self.word[i] == letter:
                        answer += 'g'
                    else:
                        if not(letter in word_elsewhere): #ie if you give twice the same letter
                            answer += 'y'
                        else:
                            if self.word.count(letter)< word.count(letter): #then I gave too many letters
                                if letter in assigned_double_letters:
                                    answer += '-'
                                else:
                                    word_out_letters = [self.word[i] for i in range(5) if word[i]!= letter ] #remove self.word indices corresponging to my double letters
                                    if letter in word_out_letters:
                                        answer += 'y'
                                    else: #then the other letter is green
                                        answer +='-'
                                    assigned_double_letters.append(letter)
                            else:
                                answer += 'y'
                else:
                    answer+='-'
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