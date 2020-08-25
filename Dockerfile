FROM ubuntu:18.04

MAINTAINER Andrew Nijmeh

RUN apt-get update -y %% \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT ["python3"]

CMD ["bot/utilitybot.py"]