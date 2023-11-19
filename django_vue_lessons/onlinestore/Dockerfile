FROM python:3.10-alpine

# Устанавливаем переменную окружения PYTHONUNBUFFERED, чтобы обеспечить вывод в реальном времени
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения и переходим в нее
RUN mkdir /app
WORKDIR /app
EXPOSE 8000
# Копируем файлы зависимостей и устанавливаем их
RUN pip install --upgrade pip 
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh 
RUN chmod +x entrypoint.sh 


# Копируем весь проект в директорию контейнера

# Опционально, выполняем миграции и собираем статические файлы приложения
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Опционально, устанавливаем команду для запуска приложения
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]