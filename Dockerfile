FROM python:3.6

ADD utilitybot-dev.py /

COPY /cogs /

COPY /events /

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

CMD ["python, utilitybot.py"]
