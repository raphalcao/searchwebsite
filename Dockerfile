FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /search
WORKDIR /search
COPY . /search/
RUN pip install -r requirements.txt
