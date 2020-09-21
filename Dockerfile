FROM python:3-ubuntu

ADD utilitybot.py /

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["./utilitybot.py" ]