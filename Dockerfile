FROM python:3.12

WORKDIR /app

COPY requirements/production.txt ./requirements/production.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r ./requirements/production.txt --no-cache-dir

COPY src/ .

RUN apt-get update && apt-get install -y nano
