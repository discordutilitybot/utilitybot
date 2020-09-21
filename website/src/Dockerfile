FROM python3.6

ADD website/src / 

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD [ "./app.py"] 