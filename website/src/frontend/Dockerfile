FROM python:3.7-onbuild

WORKDIR /src/frontend /

COPY /website/src/backend .
COPY /website/src/backend/blueprints .

# Update system dependencies and system.
RUN apt-get update && apt-get upgrade
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r --upgrade requirements.txt

ENTRYPOINT [ "python" ]
CMD ["main.py"]