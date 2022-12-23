import game as g
wordle = g.Wordle()
wordle.word = 'voter'
inputs = ['aeros','camel','tight','comic','forte','magic']
outputs = ['-yyy-','---g-','y----','-g---','-gyyy','-----']

for i,el in enumerate(inputs):
    if wordle.evaluate_guess(el)!=outputs[i]:
        raise ValueError('Game.py has an issue.')
    