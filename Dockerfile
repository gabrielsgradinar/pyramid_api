FROM python:3.8.5

WORKDIR /usr/app

COPY . .

RUN apt-get update

RUN apt-get upgrade -y

RUN pip install --upgrade pip poetry

RUN poetry install

CMD [ "make", "run-serve" ]

