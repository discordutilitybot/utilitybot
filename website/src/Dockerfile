FROM python:3.7-buster

ADD website/src 

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD [ "./app.py"] 