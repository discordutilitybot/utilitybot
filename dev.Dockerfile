# This is utilitybot.co's development docker file that will **not** be uploaded to GitHub. This is for development purposes, so there will be likely lots of errors and runtime problems that should be fixed for production

ARG version=3.6
ARG file="./bot.py"
ARG entrypoint="python3"

FROM python:$version-

WORKDIR /utilitybot /

# Update system packages and pip
RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    bzip2 \
    ca-certificates \
    curl \
    file \
    fonts-dejavu-core \
    g++ \
    git \
    less \
    libz-dev \
    locales \
\
RUN git clone https://github.com/discordutilitybot/utilitybot.git
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY /utils /
COPY /cogs / 
COPY /events /
COPY /tests /
COPY /command /

ENTRYPOINT [ $entrypoint ]
CMD [${file}]
