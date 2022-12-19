FROM python:3.6

COPY ../ ./
RUN pip3 install --no-cache-dir -r docker_requirements.txt