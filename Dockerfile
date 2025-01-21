FROM python:3.12-alpine

WORKDIR /home/app

COPY ./src /home/app/src

RUN apk update && \
    apk upgrade && \
    apk add postgresql && \
    apk add nginx && \
    apk add py3-pip

