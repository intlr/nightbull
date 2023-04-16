FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

EXPOSE 5000

CMD flask --app src/app run --host=0.0.0.0 --port=8080
