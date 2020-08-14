FROM python:latest

LABEL maintainer="Daniel Rahamim drahamim@sbin.dev"

ADD ./app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 main.py