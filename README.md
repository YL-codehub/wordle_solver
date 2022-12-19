#  Wordle-assistant-solver #

Motivation
----------
han 3,000 words describing the project and its development; including prototyping, testing, profiling etc...
Contents (optional)

Installation
------------
This project has been written with Python 3.6 and numpy 1.23 only. Any updated version of those packages should work but the author advises not to take it for granted.
You can either create the associated environment or create a container with Docker (see below).

Docker*:
- In the wordle_solver directory; creates a docker image from the Dockerfile:
```
docker build -t python36_and_numpy . 
```
- Promote the image to a container:
```
docker run -d -t --name=wordle_container python36_and_numpy 
```
- Access your container in a bash terminal:
```
docker exec -ti wordle_container bash
```
- Run your files that have been copied into the home repertory
```
python3 main.py
```
Features
--------

Principle
---------

Testing
-------

Performances
------------

Version status
--------------

--------------------------------------------------------------------------------

Yoann Launay, University of Cambridge.
Dec 2022.

--------------------------------------------------------------------------------
*Original game:
https://wordlegame.org/uk

*Installation:  
https://www.docker.com/get-started/