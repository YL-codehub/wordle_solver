# wordle_solver

Wordle-assistant-solver

Description + motivation
Contents (optional)

Installation
Docker:
#in the wordle_solver directory; creates a docker image from the Dockerfile:
docker build -t python36_and_numpy . 
#run the image :
docker run -d -t --name=wordle_container python36_and_numpy 
#Access your image in Linux mode
docker exec -ti wordle_container bash
#Run your files that have been copied into the home repertory
python3 main.py

How to run/use the project
Features
Frameworks (Languages/Testing/CI/Containerisation)
Build status / Known bugs / version info (optional)

Yoann Launay, University of Cambridge.
Dec 2022.