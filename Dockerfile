FROM python:3.6

ADD utilitybot-dev.py /

ADD /cogs /

ADD /events /

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["./utilitybot-dev.py" ]