ARG version=3.6
ARG file="./bot.py"
ARG entrypoint="python"

FROM python:$version

WORKDIR /utilitybot /

# Update system packages and pip
RUN apt-get update \
    && apt get-upgrade \
    && apt-install git \
    && apt install curl \
    && apt install python3-pip \
    && apt install yarn


RUN pip3 install --upgrade pip

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY /utils /
COPY /cogs / 
COPY /events /

ENTRYPOINT [ $entrypoint ]
CMD [${file}]
