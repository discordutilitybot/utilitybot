
FROM python:3.6

WORKDIR /bot
 
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /bot .

CMD ["python", "utilitybot.py"]