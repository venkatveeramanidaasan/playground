FROM ubuntu:latest

FROM python:3

RUN apt-get update -y
RUN apt-get install imagemagick ghostscript poppler-utils libmagickwand-dev tesseract-ocr libtesseract-dev -y
RUN apt-get install python3-dev python3-setuptools -y

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt


