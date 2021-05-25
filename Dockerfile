FROM python:3.10.0b1-buster
COPY . /carrillo-figures
WORKDIR /carrillo-figures
CMD python CreateFigs.py