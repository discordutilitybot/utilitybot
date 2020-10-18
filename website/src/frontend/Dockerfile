FROM python:3.7-onbuild

COPY . /website/src/frontend
WORKDIR /website/src/frontend .

COPY /website/src/backend .
COPY /website/src/backend/blueprints .

# Update system dependencies and system.

RUN apt-get update 
RUN apt-get upgrade
RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install -r --upgrade requirements.

EXPOSE 8080

ENTRYPOINT [ "python" ]
CMD ["main.py"]