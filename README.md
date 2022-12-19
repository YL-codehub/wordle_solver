#  Wordle Solving Assistant #

* * This file uses GitHub's Readme files syntax. Read it in the original repository online for a better experience. * *

## Motivation

[Wordle](https://wordlegame.org/uk) is a simple game based on a finite dictionnary of words with 5 letters. With the hints provided for each letter of each word guess one can converge to the right word, theoretically in a finite number of guesses, in practice sometimes with less than 6 guesses.

The motivation of this project is to provide a tool that, from the knowledge of the whole dictionnary, provides better guesses than a human and if possible below 6 guesses for most cases.

Contents (optional)

## Installation

This project has been written with Python 3.6 and numpy 1.23 only. Any updated version of those packages should work but the author advises not to take it for granted.
You can either create the associated environment or create a container with Docker (see below).

[Docker](https://www.docker.com/get-started/):

In the wordle_solver directory, create a docker image (e.g. called python36_and_numpy) from the Dockerfile:
```
docker build -t python36_and_numpy . 
```
Promote the image to a container (e.g. called wordle_container):
```
docker run -d -t --name=wordle_container python36_and_numpy 
```
Access your container in a bash terminal:
```
docker exec -ti wordle_container bash
```
Run your files that have been copied into the home repertory:
```
python3 main.py
```

## Features & Construction

prototyping and describing functions
### main.py 

## Testing and Continuous Integration
Unit tests, assert? pytest?

## Performances
time and guesses, cf autoruns

profiling ?see optimisation course.

## Version status & open problems
not completely solved; among words with one letter of difference, algorithm probably uses the most common one. 


--------------------------------------------------------------------------------

Yoann Launay, University of Cambridge.
Dec 2022.
