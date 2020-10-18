FROM python:3.7-onbuild

WORKDIR /src/frontend /

COPY /website/src/backend .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . .

ENTRYPOINT ["python"]

CMD [ "./app.py"] 
