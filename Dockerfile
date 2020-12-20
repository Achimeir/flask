FROM python:alpine AS base

LABEL MAINTAINER="Achi Shen"

# RUN apt-get update -y && apt-get install -y python3-pip

EXPOSE 80
EXPOSE 5000

COPY ./requirements.txt /RESite/requirements.txt

WORKDIR /RESite

RUN pip install -r requirements.txt

COPY . .

WORKDIR /RESite/src


ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

