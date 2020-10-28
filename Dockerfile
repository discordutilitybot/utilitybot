ARG version=3.6
FROM python:$version

WORKDIR /utilitybot /

# Update system packages and pip
RUN apt-get update \
    && apt get-upgrade \
    && apt-install git \
    && apt install curl \
RUN pip install --upgrade pip

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY /utils /
COPY /cogs / 
COPY /events /

ENTRYPOINT [" python " ]
CMD ["./utilitybot.py"]
