FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install libmagickwand-dev -y
RUN apt-get install python3-dev python3-setuptools -y

FROM python:3

WORKDIR /app

COPY . /app


RUN pip install --trusted-host pypi.python.org -r requirements.txt


