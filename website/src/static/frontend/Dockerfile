FROM python:3.7-buster

WORKDIR /src/frontend/templates

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .

ENTRYPOINT ["python"]

CMD [ "./app.py"] 
