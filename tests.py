'''unit tests to check the validity and coherence of the project.
The github continuous integration workflow uses those tests.'''

import game as g

# Testing the game outputs on random words
wordle = g.Wordle()
wordle.word = 'voter'
inputs = ['aeros','camel','tight','comic','forte','magic']
outputs = ['-yyy-','---g-','y----','-g---','-gyyy','-----'] # The following outputs are the good ones given by https://wordlegame.org/uk

for i,el in enumerate(inputs):
    if wordle.evaluate_guess(el)!=outputs[i]:
        raise ValueError('Game.py has an issue.')
    
# Testing the assistant solver
import auto_runs 
# which is enough because it tests anything in shortlist.py and tools.py,
# but also if there's a word that can't be guessed by the solver with less than 16 guesses, an error will be raised.