FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

CMD uvicorn --host '0.0.0.0' --port '8080' src.app:app
