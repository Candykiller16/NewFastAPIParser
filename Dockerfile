FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


