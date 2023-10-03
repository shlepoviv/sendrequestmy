FROM python:3.10-alpine

LABEL maintainer = "shlepov-ivan@mail.ru"

ARG ARGMARKER='companies or users or auth'
ENV MARKER=$ARGMARKER

RUN apk update && apk upgrade && apk add bash

WORKDIR /usr/t

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD  pytest -v -s tests/*