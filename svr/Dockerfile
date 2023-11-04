FROM python:3.9-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001