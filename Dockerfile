# pull official base image
FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./pricealert/requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./pricealert /app/pricealert
ADD ./api-entrypoint.sh /app/
ADD ./worker-entrypoint.sh /app/
ADD ./celery-beat-entrypoint.sh /app/

RUN chmod +x /app/api-entrypoint.sh
RUN chmod +x /app/worker-entrypoint.sh
RUN chmod +x /app/celery-beat-entrypoint.sh