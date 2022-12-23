#  Wordle Solving Assistant #

**This file uses GitHub's Readme files syntax. Read it in the original repository online for a better experience.**

## Motivation

[Wordle](https://wordlegame.org/uk) is a simple game based on a finite dictionnary of words with 5 letters. With the hints provided for each letter of each word guess, one can converge to the right word, theoretically in a finite number of guesses, in practice sometimes with less than 6 guesses.

The motivation of this project is to provide a tool that, from the knowledge of the whole dictionnary, provides better guesses than a human and if possible below 6 guesses for most cases.

## Installation

This project has been written using Python 3.8 and numpy 1.23 only. However the code passes continuous integration tests from at least 3.6 to 3.10. To execute line and memory profiling yourself (see section below), you'll need to install [pyinstrument](https://github.com/joerick/pyinstrument) line profiler and [pympler](https://pympler.readthedocs.io/en/latest/#) memory profiler.

To install those dependencies, you can create the associated environment and use in a terminal:
```
pip3 install [package]
```
for numpy, pyinstrument and pympler.

Alternatively you can create a container with Docker from the provided Dockerfile (see below).

[Docker](https://www.docker.com/get-started/): in a terminal, in the wordle_solver directory, create a docker image (e.g. called python36_wordle) from the Dockerfile:
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
Thinking the construction of this project was based on the following recquirements:

>- Suggesting a first guess
>- Suggesting subsequent guesses based on the response until it can correctly guess the word.
>- Your version doesn't not have to be limited to 6 guesses but can continue until the puzzle is solved.
>- Should be able to be run in batch (where the correct word is provided as an input) or interactively with the user providing the guess and response
>- Be version controled and connected to some hosting site (public or private) with README and Licence files.
>- Be Modular, clearly written with sensible variable names and contain documentation
>- Contain unit tests and linked to some continuous integration framework to run them automatically
>- Be performant (ie: the interactive version works on human timescales, so a maximum of 1-2 seconds to generate a guess)
>- Be portable, so both code and enviroment can be replicated on other machines, ie using Docker.


### Construction philosophy
blabla, invention process.

### Files summary

#### main.py 
#### shortlist.py
#### tools.py
#### game.py
#### auto_runs.py
This is the only file that requires your modifications.

## Testing and Continuous Integration
blabla.

## Performances
Since **auto_runs.py** is using all components of our work, it is relevant to apply time, line and memory profiling there. We chose to use [pyinstrument](https://github.com/joerick/pyinstrument) and [pympler](https://pympler.readthedocs.io/en/latest/#) and also simple timers with the native **time** package.

An example of output from **auto_runs.py** with profilers all turned on:
```
Average number of guesses : 3.980690507453464
Number of words for each performance :
Guesses to solve | % Words  | Cumulated %
        0           0.01        0.01
        1           1.32        1.33
        2           14.71       16.03
        3           30.66       46.70
        4           23.95       70.65
        5           13.54       84.19
        6           7.56        91.75
        7           3.87        95.62
        8           2.09        97.71
        9           1.16        98.87
        10          0.58        99.45
        11          0.31        99.76
        12          0.13        99.89
        13          0.08        99.97
        14          0.02        99.99
        15          0.01        100.00
        16          0.00        100.00
        17          0.00        100.00
        18          0.00        100.00
        19          0.00        100.00
Average time per guess : 0.00061  seconds.
--------------------------------------------------------------
Line profiling:

  _     ._   __/__   _ _  _  _ _/_   Recorded: 10:38:22  Samples:  511599
 /_//_/// /_\ / //_// / //_'/ //     Duration: 32.576    CPU time: 32.549
/   _/                      v3.4.2
│  ├─ 21.184 intersection_grey  shortlist.py:63
│  │  ├─ 19.086 [self]
│  │  └─ 2.098 sum  <__array_function__ internals>:2
│  │        [18 frames hidden]  <__array_function__ internals>, numpy...
│  ├─ 6.803 intersection_yellow  shortlist.py:102
│  │  ├─ 5.063 [self]
│  │  └─ 1.740 sum  <__array_function__ internals>:2
│  │        [18 frames hidden]  <__array_function__ internals>, numpy...
│  └─ 3.123 intersection_green  shortlist.py:86
│     └─ 3.121 [self]
└─ 0.696 evaluate_guess  game.py:12
   └─ 0.690 [self]


--------------------------------------------------------------
Memory profiling:
                       types |   # objects |   total size
============================ | =========== | ============
                         str |     2054203 |    255.88 MB
                        list |      512375 |     56.58 MB
                       tuple |      516360 |     31.53 MB
                       float |      563271 |     12.89 MB
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
```
## Version status & open problems
The current repository is the original version of the code (v0). Hereby, the author states that there won't be any more releases for future updates from himself starting from 1/1/23. 

However, the author would like to make a few suggestions on possible improvements that could be made in future uses of this code:
- the current version does not find all words within 6 guesses. For a few words, multiple words are indeed similar to them with only one unique letter; the algorithm has no other choice than proposing most of the words in this set. On the other hand, the author identify a possible bias in the secret word's choice by Wordle: within a list of almost identical words; the secret one is usually the most common one in human interactions. This means that the solver could stop doing arbitrary choices in such cases by e.g. using the google words' use ranking.
- the assistant would obviously benefits from a GUI other than the terminal's.
- if the algorithm is generalized to longer words, we would certainly need better time performance, e.g. by using better parallel processes and not just restricting it to numpy's use.
--------------------------------------------------------------------------------

Yoann Launay, University of Cambridge.
Dec 2022.
