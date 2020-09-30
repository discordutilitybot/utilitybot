FROM python:3.7

WORKDIR /src/frontend/templates

ADD /src/statoc/backend /

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8081

COPY . .

ENTRYPOINT ["python"]

CMD [ "./main.py"] 
