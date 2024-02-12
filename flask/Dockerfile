FROM python:3.12.2-bookworm

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["uwsgi", "app.ini"]
