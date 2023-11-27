# javascript runtime
FROM node:17-alpine AS builder

# Add a work directory
WORKDIR /opt/word_couch

FROM python:3.8-buster

RUN mkdir -p /var/log/word_couch

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD /bin/sh -c ./start.sh
