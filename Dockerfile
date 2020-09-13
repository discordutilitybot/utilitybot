FROM python:3

ADD utilitybot.py /

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./utilitybot.py" ]