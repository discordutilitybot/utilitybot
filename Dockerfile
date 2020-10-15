FROM python:3.6-onbuild

WORKDIR /utilitybot /

RUN apt-get update && apt-get upgrade

# install python dependencies

RUN pip install --upgrade pip
# Copy requirements.txt and its depedencies
COPY ./requirements.txt . 
# Install depedencies 
RUN pip install -r requirements.txt

COPY /utils
COPY /cogs
COPY /events

ENTRYPOINT [" python " ]

CMD ["./utilitybot.py"]
