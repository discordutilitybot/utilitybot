FROM python:3.7

WORKDIR /src/backend /

COPY /src/frontend/templates /

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8081

COPY . .

ENTRYPOINT ["python"]

CMD [ "./main.py"] 
