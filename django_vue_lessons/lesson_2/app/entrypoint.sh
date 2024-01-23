#!/bin/sh


echo "Waiting for database..."

if [ "$SQL_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Database started"


# Очистить бд 
# python manage.py flush --no-input

python manage.py makemigrations

python manage.py migrate 



# python manage.py collectstatic --noinput

# if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
#   echo "Creating superuser..."
#   python manage.py createsuperuser --no-input \
#     --username $DJANGO_SUPERUSER_USERNAME \
#     --email $DJANGO_SUPERUSER_EMAIL
#   echo "from django.contrib.auth.models import User; User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').update(password='$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
# fi


exec "$@"