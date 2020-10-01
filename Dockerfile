FROM python:3.6-onbuild

ADD utilitybot.py /

ADD /utils /

ADD /cogs /

ADD /events /

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["./utilitybot.py" ]