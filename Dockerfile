FROM python:3.10.7-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as build

RUN apt-get update
RUN apt-get install python3-pip -y

RUN pip3 install --upgrade pip
RUN pip3 install "poetry==1.1.12"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

FROM base as deploy

EXPOSE 1337

ENV PATH="/venv/bin:${PATH}"
ENV VIRTUAL_ENV="/venv"

RUN apt-get update

COPY --from=build /venv /venv
COPY . /app

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "1337"]
