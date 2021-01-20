
ARG version=3.6
ARG file="./bot.py"
ARG entrypoint="python3"

FROM python:$version

WORKDIR /utilitybot /

# Update system packages and pip
RUN pip3 install --upgrade pip

RUN git clone https://github.com/discordutilitybot/utilitybot.git
COPY requirements.txt . 
RUN pip3 install -r requirements.txt

COPY /utils /
COPY /cogs / 
COPY /events /
COPY /tests /
COPY /command /

ENTRYPOINT [ $entrypoint ]
CMD [${file}]
