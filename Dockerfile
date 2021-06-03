FROM python:3.8.5

WORKDIR /usr/app

COPY pyproject.toml .
COPY poetry.lock .

RUN apt-get update
RUN apt-get upgrade -y

RUN pip install --upgrade pip poetry

COPY . .

RUN poetry install

RUN ls


CMD [ "make", "run-serve" ]

