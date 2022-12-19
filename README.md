#  Wordle Solving Assistant #

## Motivation

[Wordle](https://wordlegame.org/uk) han 3,000 words describing the project and its development; including , testing, profiling etc...
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

## Testing


## Performances

## Version status & open problems


--------------------------------------------------------------------------------

Yoann Launay, University of Cambridge.
Dec 2022.
