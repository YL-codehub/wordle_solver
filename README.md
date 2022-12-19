############################
#  Wordle-assistant-solver #
############################

Motivation
----------
han 3,000 words describing the project and its development; including prototyping, testing, profiling etc...
Contents (optional)

Installation
------------
This project has been written with Python 3.6 and numpy 1.23 only.
You can either create the associated environment or create a container with Docker (see below).

Docker*:
In the wordle_solver directory; creates a docker image from the Dockerfile:
docker build -t python36_and_numpy . 
#run the image :
docker run -d -t --name=wordle_container python36_and_numpy 
#Access your image in Linux mode
docker exec -ti wordle_container bash
#Run your files that have been copied into the home repertory
python3 main.py

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

Yoann Launay, University of Cambridge.
Dec 2022.

--------------------------------------------------------------------------------
*Original game:
https://wordlegame.org/uk
*Installation:  
https://www.docker.com/get-started/