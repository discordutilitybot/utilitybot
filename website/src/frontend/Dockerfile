FROM python:3.7

WORKDIR /src/frontend/templates

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .

ENTRYPOINT ["python"]

CMD [ "./app.py"] 
