'''shortlist class'''
import numpy as np
import tools as tl

class Shortlist:
    """Class representing an updatable shortlist of guesses."""
    def __init__(self):
        # Initial untouched values 
        self.words = []
        self.words_splitted = []
        self.scores = []

        # Temporary variables, updatable
        self.temp_words = [] 
        self.temp_words_splitted = []
        self.temp_scores = []

        # Knowledge from Wordle hints, dictionaries (letter, list of places).
        self.temp_grey_letters = {} 
        self.temp_green_letters = {} 
        self.temp_yellow_letters = {}
    
    def reset_all_temp(self):
        '''None ---> None. 
        Resets all temp_ self.variables to their value before starting guesses.'''
        self.temp_grey_letters = {}
        self.temp_green_letters = {}
        self.temp_yellow_letters = {}
        self.temp_words = self.words
        self.temp_words_splitted = self.words_splitted
        self.temp_scores = self.scores

    def best_guess(self, print_ = False):
        ''' None ---> None.
        Returns the word with the best score in the temp_words shortlist.
        Prints the result if print_ = True.'''
        if len(self.temp_words)>0:
            temp = self.temp_words[0]
            if print_:
                print('Best guess :',temp)
            return temp

    def print_top(self):
        ''' None ---> None.
        Prints the 9 words with the best scores in the temp_words shortlist.'''    
        print('----------------------------------')
        print('| Suggestions |   Score   | Rank |')
        print('----------------------------------')
        for i in range(min(9,len(self.temp_words))):
            print('|    '+self.temp_words[i]+ '    |  '+'{:.4f}'.format(self.temp_scores[i])+'  |   '+str(i+1)+'  |' )

    def read_1st_guess(self):
        '''None ---> None.
        Reads words_ranked.txt's initial scoring and assigns it to initial variables.'''
        tab= np.loadtxt('words_ranked.txt',dtype='str')
        self.words = tab[:,0]
        self.temp_words = self.words
        self.scores = tab[:,1].astype(float)
        self.temp_scores = self.scores
        self.words_splitted = tl.split_in_array(self.words)
        self.temp_words_splitted = self.words_splitted

    def intersection_grey(self):
        '''None ---> None.
        Updates the shortlist in temp_words from temp_grey_letters.
        Words with the grey letters are removed from the shortlist.'''
        # Initialize selection boolean array
        Truth = 0
        for letter in self.temp_grey_letters:
            temp = (self.temp_words_splitted == letter)            
            # If the letter is also a green or yellow letter
            if letter in self.temp_green_letters:
                # We don't study columns where there is a detected green.
                temp[:,self.temp_green_letters[letter]] *= False 
            if letter in self.temp_yellow_letters:
                #  We study columns where there is a detected yellow but in intersection_yellow.
                return() 
            Truth +=  temp
        Or = np.sum(Truth,axis = 1) # number of found grey letters per word 
        Truth = (Or == 0) # keep only those without any
        # Update temp arrays by using numpy selection
        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def intersection_green(self):
        '''None ---> None.
        Updates the shortlist in temp_words from temp_green_letters.
        Only words with the green letters at the right spots are kept in the shortlist.'''
        # Initialize selection boolean array
        Truth = 1
        # Each word of the shortlist has to have the green letters at the right places
        # No need for extra considerations if doublons
        for letter, positions in self.temp_green_letters.items():
            for pos in positions:
                Truth = np.logical_and(Truth, self.temp_words_splitted[:,pos] == letter)
        # Update temp arrays by using numpy selection
        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def intersection_yellow(self):
        '''None ---> None.
        Updates the shortlist in temp_words from temp_yellow_letters.
        Only words with the yellow letters at the right spots are kept in the shortlist.'''
        # Initialize selection boolean array
        Truth = 1
        for letter in self.temp_yellow_letters: 
            # If the letter is yellow and has a doublon, the selection array must not use those columns for selection
            # cols = indices excluding columns with this letter
            # cols2 = indices excluding columns with this letter as green or grey only       
            if letter in self.temp_green_letters:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter])-set(self.temp_green_letters[letter])) 
                cols2 = list(set(self.temp_yellow_letters[letter])-set(self.temp_green_letters[letter]))
            elif letter in self.temp_grey_letters:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter])-set(self.temp_grey_letters[letter]))
                cols2 = list(set(self.temp_yellow_letters[letter])-set(self.temp_grey_letters[letter]))
            else:
                cols = list(set(range(0,5))-set(self.temp_yellow_letters[letter]))
                cols2 = self.temp_yellow_letters[letter]

            # We select words where columns without the identified doublon and yellow column have the yellow letter
            auxTruth = (self.temp_words_splitted[:,cols] == letter)
            Or = np.sum(auxTruth, axis = 1)
            auxTruth = (Or > 0 ) 

            # We select words where the yellow letter is not at the input spot
            auxTruth2 = (self.temp_words_splitted[:,cols2]==letter)
            Or2 = np.sum(auxTruth2, axis = 1)
            auxTruth2 = (Or2 == 0)

            # We intersect the two boolean array
            Truth = np.logical_and(Truth, auxTruth)
            Truth = np.logical_and(Truth, auxTruth2)

        # Update temp arrays by using numpy selection
        self.temp_words = self.temp_words[Truth]
        self.temp_words_splitted = self.temp_words_splitted[Truth]
        self.temp_scores = self.temp_scores[Truth]

    def clear_temp_letters(self):
        '''None ---> None.
        Clears temporary letter variables.'''
        self.temp_grey_letters = {}
        self.temp_green_letters = {}
        self.temp_yellow_letters = {}

    def new_temp(self, word, output):
        '''(str,str)--->None.
        From a given word and its Wordle output, assigns letters to their dictionnary (g,y or -).'''
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
            else:
                if word[i] in self.temp_yellow_letters:
                    self.temp_yellow_letters[word[i]].append(i)
                else:
                    self.temp_yellow_letters[word[i]]= [i]


    def shorting_from_output(self,word,output):
        '''(str,str)--->None.
        From a given word and its Wordle output, completes the update of the shortlist.'''
        self.new_temp(word,output)
        # Green, grey, yellow order is important as explained in interesection_ functions
        if self.temp_green_letters != {}:
            self.intersection_green()
        if self.temp_grey_letters != {}:
            self.intersection_grey()
        if self.temp_yellow_letters != {}:
            self.intersection_yellow()
    
    def update_scoring(self):
        '''None ---> None.
        Updates the scores with a scoring on the shortlist rather than on the full dictionnary.
        See tools.rank_words.'''
        self.temp_words, self.temp_words_splitted, self.temp_scores = tl.rank_words(self.temp_words,self.temp_words_splitted)


'''Yoann Launay, University of Cambridge, 12/22.'''