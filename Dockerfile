FROM python:latest

WORKDIR /scrapperPy

RUN pip3 install requests bs4 mysql-connector-python

COPY *.py .