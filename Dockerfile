FROM python:3

WORKDIR /game

COPY requirements.txt /game/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /game

RUN apt-get update

RUN apt-get install socat -y

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python /game/main.py"
