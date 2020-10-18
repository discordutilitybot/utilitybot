FROM python:3.7-onbuild

COPY . /website/src/backend
WORKDIR /website/src/backend .

COPY /website/src/frotend .
COPY /website/src/backend/templates .

# Update system dependencies and system.

RUN apt-get update 
RUN apt-get upgrade
RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install -r --upgrade requirements.txt

EXPOSE 8081

ENTRYPOINT [ "python" ]
CMD ["main.py"]