FROM python:3.8.3-slim

RUN mkdir /app \
 && cd app
COPY requirements.txt /app

RUN pip install -U pip \
 && pip install -r /app/requirements.txt

COPY ./app /app

ENTRYPOINT ["python", "-m","app.main", "upload"]