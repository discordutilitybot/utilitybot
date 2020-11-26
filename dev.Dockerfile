# This is utilitybot.co's development docker file that will **not** be uploaded to GitHub. This is for development purposes, so there will be likely lots of errors and runtime problems that should be fixed for production

ARG version=3.6
ARG file="./bot.py"
ARG entrypoint="python"

FROM python:$version

WORKDIR /utilitybot /

# Update system packages and pip
RUN pip3 install --upgrade pip

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY /utils /
COPY /cogs / 
COPY /events /

ENTRYPOINT [ $entrypoint ]
CMD [${file}]
