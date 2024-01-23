#!/bin/sh


echo "Waiting for database..."

# while ! nc -z $DB_HOST $DB_PORT; do   
#   sleep 0.1
# done

echo "Database started"

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