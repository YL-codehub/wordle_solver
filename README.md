#  Wordle Solving Assistant 

_This file uses GitHub's Readme files syntax. Read it in the original [repository online](https://github.com/YL-codehub/wordle_solver) for a better experience._

## Motivation

[Wordle](https://wordlegame.org/uk) is a simple game based on a finite dictionnary of words with 5 letters. With the hints provided for each letter of each word guess, one can converge to the right word, theoretically in a finite number of guesses, in practice sometimes with less than 6 guesses.

The motivation of this project is to provide a tool that, from the knowledge of the whole dictionnary, provides better guesses than a human and if possible below 6 guesses for most cases.

## Installation

This project has been written using Python 3.8 and [_numpy_](https://numpy.org/doc/stable/index.html) 1.23 package only. However the code passes continuous integration tests from at least 3.6 to 3.10. To execute line and memory profiling yourself (see section below), you'll need to install [_pyinstrument_](https://github.com/joerick/pyinstrument) line profiler and [_pympler_](https://pympler.readthedocs.io/en/latest/#) memory profiler.

To install those dependencies, you can create the associated environment and use in a terminal:
```
pip3 install [package]
```
for numpy, pyinstrument and pympler.

Alternatively you can create a container with Docker from the provided Dockerfile (see below) which contains all the necessary packages.

[Install Docker](https://www.docker.com/get-started/) and once running, start a terminal and create a docker image (e.g. called python36_wordle) from the Dockerfile in the wordle_solver directory:
```
docker build -t python36_wordle . 
```
Promote the image to a container (e.g. called wordle_container):
```
docker run -d -t --name=wordle_container python36_wordle 
```
Access your container in a bash terminal:
```
docker exec -ti wordle_container bash
```
Run your files that have been copied into the home repertory:
```
python3 main.py
```
The Dockerfile is set for a Python 3.6 version: you can change it to a more recent one if needed.

## Features & Construction
### Construction philosophy
Thinking the construction of this project was based on the following recquirements:
>- Suggesting a first guess
>- Suggesting subsequent guesses based on the response until it can correctly guess the word.
>- Version doesn't not have to be limited to 6 guesses but can continue until the puzzle is solved.
>- Should be able to be run in batch (where the correct word is provided as an input) or interactively with the user providing the guess and response
>- The official list of all 5 letter words that wordle accepts is provided.
>- Being version controled and connected to some hosting site (public or private) with README and Licence files.
>- Being Modular, clearly written with sensible variable names and contain documentation
>- Containing unit tests and linked to some continuous integration framework to run them automatically
>- Being performant (ie: the interactive version works on human timescales, so a maximum of 1-2 seconds to generate a guess)
>- Being portable, so both code and enviroment can be replicated on other machines, ie using Docker.

In this context, the 1st guess has been implemented independently and raised the necessity of a word scoring library. After that, the continuous shortlisting has been encoded into an exhaustive class. The 3rd step was then to implement the interaction with the user and testing on a few words with wordle in parallel on the navigator. Finally, the test against all words has been implemented by implementing wordle outputs to avoid the human interface between the solver and the game. 

### Files summary
In addition to files and functions being all documented and steps being explained when necessary, general comments for each file of the repository are provided in the following.
#### main.py 
As its name suggests, this file is the file to run to start interacting with the solver. It loops until the user decides to exit this elementary bash interface. At each step, a top guesses list is proposed thanks to _shortlist.py_ and ask for the user's choice and the output of wordle for this guess. For each wordle output given to _main.py_, the shorlist is updated with those hints.

Note that the scoring method can be changed at each guess by setting
```
continuous_scoring = True
```
It means that the appearances score of each letter is calculated within the shortlist rather than only initially with the whole dictionary. However this has been turned off because appeared to have poorer performances in time and average guesses.
#### shortlist.py
This file contains the Shorlist class with all methods that allow to use hints from wordle output to shorten the shortlist. Some methods also use the scoring library _tools.py_. This file is the heart of the solver.
#### tools.py
This is a simple and short library of secondary functions that allow splitting arrays of words into letters, ranking letters w.r.t their appearances, ranking words as potential guesses w.r.t to their diversity or their letters or writing the first ranking etc. 
#### game.py
It contains the Wordle class; a class that allows to re-create the hint outputs of the original game given a guess and without using any API to connect online. It uses the exact same rules and has been tested successfully many times. As explained below, the success of _auto_runs.py_ is strongly suggesting its correctness. 
#### auto_runs.py
This code runs the solver against all words of the 5-words dictionary (_words.txt_). For each secret word, the code won't stop until equality with the solver's guess or until reaching 16 guesses (as 15 has been found to be the worst case). If more than 16 guesses are needed for a given secret word, an error will be raised. Different time and memory performances are implemented; line and memory profiling can be turned on by setting their Boolean variables at the start of the file:
```
line_profiling = True
memory_profiling = True
```

## Testing and Continuous Integration
In addition to multiple unit tests of each function and module and to many games successfully played, the successful execution of _auto_runs.py_ is a strong proof of the validity of this code: all words can be found in a finite amount of time and guesses and all modules are coherent.

This is the reason why any modification of this repository should pass on Python 3.6+ versions both a test of _game.py_ on a few words and an import of _auto_runs.py_ (to which one can add usual Lint checks for syntaxe mistakes). The reasonable --but not exhaustive-- choice we've made is to report any push that does not fulfill these tests through the continuous integration framework provided by Github workflow (see _.github\workflows/continuous_integration.yml_). The present version (v0) perfectly satisfies it. How good it does it is an another question that is answered in the next section.

## Performances
Since _auto_runs.py_ is using all components of our work, it is relevant to apply time, line and memory profiling there. We chose to use [_pyinstrument_](https://github.com/joerick/pyinstrument) and [_pympler_](https://pympler.readthedocs.io/en/latest/#) and also simple clocks with the native _time_ package.

An example of output from _auto_runs.py_ with profilers all turned on and on a personal laptop configuration (8GB Ram, Intel i5, Dell) is:
```
--------------------------------------------------------------
Line profiling:

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:45:24  Samples:  538483
 /_//_/// /_\ / //_// / //_'/ //     Duration: 33.730    CPU time: 33.720
/   _/                      v3.4.2

Program: auto_runs.py

33.730 <module>  auto_runs.py:1
├─ 32.440 shorting_from_output  shortlist.py:170
│  ├─ 21.781 intersection_grey  shortlist.py:63
│  │  ├─ 19.641 [self]
│  │  └─ 2.140 sum  <__array_function__ internals>:2
│  │        [18 frames hidden]  <__array_function__ internals>, numpy...
│  ├─ 7.190 intersection_yellow  shortlist.py:102
│  │  ├─ 5.108 [self]
│  │  └─ 2.081 sum  <__array_function__ internals>:2
│  │        [18 frames hidden]  <__array_function__ internals>, numpy...
│  └─ 3.199 intersection_green  shortlist.py:86
│     └─ 3.196 [self]
└─ 0.685 evaluate_guess  game.py:12
   └─ 0.678 [self]


--------------------------------------------------------------
Memory profiling:
                       types |   # objects |   total size
============================ | =========== | ============
                         str |     2181001 |    271.07 MB
                        list |      539259 |     60.04 MB
                       tuple |      543244 |     33.17 MB
                       float |      590155 |     13.51 MB
                        dict |        5116 |      2.17 MB
                        code |        6377 |    900.05 KB
                        type |         959 |    773.16 KB
               numpy.ndarray |          45 |    358.82 KB
                         set |         750 |    234.06 KB
          wrapper_descriptor |        2134 |    166.72 KB
                     weakref |        1623 |    126.80 KB
           method_descriptor |        1331 |     93.59 KB
                 abc.ABCMeta |          89 |     86.82 KB
  builtin_function_or_method |        1226 |     86.20 KB
           getset_descriptor |         976 |     68.62 KB
--------------------------------------------------------------
Average number of guesses : 3.980690507453464
Number of words for each performance :
Guesses to solve | % Words  | Cumulated %
        0           0.01        0.01
        1           1.32        1.33
        2           14.71        16.03
        3           30.66        46.70
        4           23.95        70.65
        5           13.54        84.19
        6           7.56        91.75
        7           3.87        95.62
        8           2.09        97.71
        9           1.16        98.87
        10           0.58        99.45
        11           0.31        99.76
        12           0.13        99.89
        13           0.08        99.97
        14           0.02        99.99
        15           0.01        100.00
        16           0.00        100.00
Average time per guess : 0.00063  seconds.
```
### Overall time performance
The last third of the performance output gives excellent news:
- The average number of guesses is **3.98** < 6.
- 91.75% of the words of the dictionary are guessed within 6 guesses, 99.45% within 10.
- The average time per guess is 0.6 ms and is more than acceptable for a random user. Note that the 1st guess demands 90ms, which is still more than enough to play live.

However, we note that a few words can demand 6 to 15 guesses for the solver. This issue will be adressed in the last section and is left aside for v0: the author recommands the player to always use the words they know in a list of equally scored words.  In fact, it seems to augment their chances to stay within 6 guesses as Wordle could have a biased choice for the secret word.

### Time performance per line
The line profiler output is given in the first part of the output flow and has to be read carefully; it shows the total time spent on each part of the code over the whole dictionnary and shows only the most used lines. Because it uses numpy boolean selection on consequent arrays (at most 12947x5), _intersection_ functions were expected to be the longest to run, despite the really appreciable performances provided by _numpy_ libraries. 

The hierachy between colors is coherent with the fact that grey inputs are more probable than yellow ones, the latter more probable than green ones: hence more calls for the grey ones and hence an idea of those probabilities. 

At second place, we find the game calls and is negligible compared to the shortlist calls.
 
All those times become ridiculous once divided by the number of words scanned in this script, which justifies an excellent overall performance. 

### Memory use performance
On the interpretation of the middle flow section about memory use, one has to be careful again since redundant elements are created in this test file looping on all words. Keeping a relative approach, strings and lists that sometimes contain our 12947 words or 12947x5 letters can become pretty heavy.

It is true that some information is redundant in this code as testifies the long list of used structures. However the assignements to new variables have been kept minimal in the code and the overall used memory for a single word guess (calculated separately as <5MB) is manageable by a personal laptop and does not properly threatens the speed of the code.

## Version status & open problems
The current repository is the original version of the code (v0). Hereby, the author states that there won't be any more releases for future updates from himself starting from 01/01/23. 

However, the author would like to make a few suggestions on possible improvements that could be made in future uses of this code:
- the current version does not find all words within 6 guesses. For a few words, multiple words are indeed similar to them with only one unique letter; the algorithm has no other choice than proposing most of the words in this set. On the other hand, the author identified a possible bias in the secret word's choice by Wordle: within a list of almost identical words; the secret one is usually the most common one in human interactions. This means that the solver could stop doing arbitrary choices in such cases by e.g. using the google words' use ranking.
- the assistant would obviously benefits from a GUI other than the terminal's.
- if the algorithm is generalized to longer words, we would certainly need better time performance, e.g. by using better parallel processes and not just restricting it to numpy's use.
--------------------------------------------------------------------------------

Yoann Launay, University of Cambridge.
Dec 2022.
