FROM python:3.9-slim-buster
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
WORKDIR /
COPY / /
COPY ./requirements.txt .
RUN pip install -r /requirements.txt

EXPOSE 5000