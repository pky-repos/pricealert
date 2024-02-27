#!/bin/sh

until cd /app/pricealert/
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A pricealert beat --loglevel=info