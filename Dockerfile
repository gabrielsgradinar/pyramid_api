FROM python:3.8.5

RUN apt-get update
RUN apt-get upgrade -y

RUN pip install --upgrade pip poetry gunicorn paste pastedeploy

COPY pyproject.toml /app/
COPY poetry.lock /app/

WORKDIR /app

RUN poetry install

COPY . /app/

RUN poetry install

CMD [ "make", "run-serve"]