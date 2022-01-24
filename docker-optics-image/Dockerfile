# syntax=docker/dockerfile:1

FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .