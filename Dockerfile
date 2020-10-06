FROM python:3.6-onbuild

ADD utilitybot-dev.py /

ADD /utils /

ADD /cogs /

ADD /events /

COPY requirements.txt .

pip install requirements.txt
ENTRYPOINT [ "python" ]

CMD ["./utilitybot-dev.py" ]