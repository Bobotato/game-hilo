FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN apt-get update

RUN apt-get install socat -y

CMD "python /app/main.py"
