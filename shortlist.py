'''shortlist class'''
import numpy as np
import tools as tl

class Shortlist:
    """ Class maintening remaining possibilities  """
    def __init__(self):
        self.words = []
        self.words_splitted = []
        self.scores = []
        # self.grey_letters = [] # list.
        # self.green_letters = {} #dictionary numb letter, letter
        # self.yellow_letters = {} #dictionary letter , places where they're not.
    
        self.temp_words = []
        self.temp_words_splitted = []
        self.temp_scores = []
        self.temp_grey_letters = {} #dictionary letter , places where they're not.
        self.temp_green_letters = {} #dictionary numb letter, letter
        self.temp_yellow_letters = {} #dictionary letter , places where they're not.
    
    def reset_all_temp(self):
        self.temp_grey_letters = {}
        self.temp_green_letters = {}
        self.temp_yellow_letters = {}
        self.temp_words = self.words
        self.temp_words_splitted = self.words_splitted
        self.temp_scores = self.scores

    def best_guess(self, print_ = False):
        '''print best suggestion'''
        if len(self.temp_words)>0:
            temp = self.temp_words[0]
            if print_:
                print('Best guess :',temp)
            return temp

    def print_top(self):
        '''Top 9 suggestions'''    
        print('----------------------------------')
        print('| Suggestions |   Score   | Rank |')
        print('----------------------------------')
        for i in range(min(9,len(self.temp_words))):
            print('|    '+self.temp_words[i]+ '    |  '+'{:.4f}'.format(self.temp_scores[i])+'  |   '+str(i+1)+'  |' )

    def read_1st_guess(self):
        '''Reads our work from score.py'''
        tab= np.loadtxt('words_ranked.txt',dtype='str')
        self.words = tab[:,0]
        self.temp_words = self.words
        self.scores = tab[:,1].astype(np.float)
        self.temp_scores = self.scores
        self.words_splitted = tl.split_in_array(self.words)
        self.temp_words_splitted = self.words_splitted

    # def temp_to_global(self):
    #     '''from temp var to general ones.'''
    #     self.grey_letters += self.temp_grey_letters

    #     for letter, pos in self.temp_green_letters.items():
    #         self.green_letters[letter] = pos

    #     for letter, pos in self.temp_yellow_letters.items():
    #         if not(letter in self.yellow_letters):
    #             self.yellow_letters[letter] = pos
    #         else:
    #             self.yellow_letters[letter] = list(set(self.yellow_letters[letter])+set(pos))

    def intersection_grey(self):
        '''use temp_grey_letters to update temp_words'''
        Truth = 0
        for letter in self.temp_grey_letters:
            temp = (self.temp_words_splitted == letter)            
            if letter in self.temp_green_letters:
                temp[:,self.temp_green_letters[letter]] *= False # so that we don't check columns where there is a green.
            if letter in self.temp_yellow_letters:
                return() # so that we don't check where there is a yellow, will be handled in yellow intersection.
            Truth +=  temp
        Or = np.sum(Truth,axis = 1)
        Truth = (Or == 0)
        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def intersection_green(self):
        '''use temp_green_letters to update temp_words'''
        Truth = 1
        for letter, positions in self.temp_green_letters.items():
            for pos in positions:
                Truth = np.logical_and(Truth, self.temp_words_splitted[:,pos] == letter)
        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def intersection_yellow(self):
        '''use temp_yellow_letters to update temp_words''' 
        Truth = 1
        for letter in self.temp_yellow_letters: 
            #it is somewhere else but not where green or grey is          
            if letter in self.temp_green_letters:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter])-set(self.temp_green_letters[letter])) 
                cols2 = list(set(self.temp_yellow_letters[letter])-set(self.temp_green_letters[letter]))
            elif letter in self.temp_grey_letters:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter])-set(self.temp_grey_letters[letter]))
                cols2 = list(set(self.temp_yellow_letters[letter])-set(self.temp_grey_letters[letter]))
            else:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter]))
                cols2 = self.temp_yellow_letters[letter]

            auxTruth = (self.temp_words_splitted[:,cols] == letter)
            Or = np.sum(auxTruth, axis = 1)
            auxTruth = (Or > 0 ) #only one in total

            auxTruth2 = (self.temp_words_splitted[:,cols2]==letter)
            Or2 = np.sum(auxTruth2, axis = 1)
            auxTruth2 = (Or2 == 0)

            Truth = np.logical_and(Truth, auxTruth)
            Truth = np.logical_and(Truth, auxTruth2)

        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def clear_temp_letters(self):
        self.temp_grey_letters = {}
        self.temp_green_letters = {}
        self.temp_yellow_letters = {}

    def new_temp(self, word, output):
        '''define new temp var'''
        self.clear_temp_letters()
        for i in range(5):
            if output[i]=='-':
                if word[i] in self.temp_grey_letters:
                    self.temp_grey_letters[word[i]].append(i)
                else:
                    self.temp_grey_letters[word[i]]= [i]
            elif output[i]=='g':
                if word[i] in self.temp_green_letters:
                    self.temp_green_letters[word[i]].append(i)
                else:
                    self.temp_green_letters[word[i]]= [i]
            else: #yellow case
                if word[i] in self.temp_yellow_letters:
                    self.temp_yellow_letters[word[i]].append(i)
                else:
                    self.temp_yellow_letters[word[i]]= [i]


    def shorting_from_output(self,word,output):
        ''' read someting like 'women' and '-yg-y' '''
        self.new_temp(word,output)
        if self.temp_green_letters != {}:
            self.intersection_green()
        if self.temp_grey_letters != {}:
            self.intersection_grey()
        if self.temp_yellow_letters != {}:
            self.intersection_yellow()
        # print(self.temp_green_letters)
        # print(self.temp_yellow_letters)
        # print(self.temp_grey_letters)
        # # # self.temp_to_global()
    
    def update_scoring(self):
        self.temp_words, self.temp_words_splitted, self.temp_scores = tl.rank_words(self.temp_words,self.temp_words_splitted)