#!/bin/sh

until cd /app/pricealert/
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A pricealert worker --loglevel=info --concurrency 1 -E