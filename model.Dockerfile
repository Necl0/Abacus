FROM python:3.9.15-alpine3.15

WORKDIR /usr/src/app

COPY requirements.txt .

COPY . .

RUN apk add curl

RUN pip install -r requirements.txt 

CMD ["python", "app.py"]
