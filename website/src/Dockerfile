FROM python:3.7-buster

ADD app.py /d

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]

CMD [ "./app.py"] 