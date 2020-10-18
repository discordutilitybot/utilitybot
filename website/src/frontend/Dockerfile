FROM python:3.7-onbuild

WORKDIR /src/frontend /

COPY /website/src/backend .

# Update system dependencies and system.
RUN apt-get update && apt-get upgrade