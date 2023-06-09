until cd /app/backend
until python3 ./manage.py migrate
do
    sleep 2
done

./manage.py collectstatic --noinput

gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
