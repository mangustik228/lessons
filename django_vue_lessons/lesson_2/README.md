# First step 
**[Хорошая статья](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

```bash 
mkdir new_project 
cd new_project 
cp somewhere/docker-compose.yml docker-compose.yml 
cp somewhere/.env .env 
django-admin startproject project_name 
``` 

## Setup `vscode`

- Open `Run and Debug`
- Create `launch.json` -> Python -> Django 

### File `.vscode/launch.json`: 

```bash 
    # need to change
    "program": "${workspaceFolder}/manage.py",
    # to
    "program": "${workspaceFolder}/app/manage.py",

    # add args (if not exist): 
    "--noreload"

    # need to comment args (if exist): 
    // "--nothreading"

```

### UPGRADE `app/app/settings.py`: 

```bash 
SECRET_KEY = os.environ.get("SECRET_KEY")
MODE = os.environ.get("MODE")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

```


```python 
# Для postgres (app/settings.py): 
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

```


## Сериализация `app.app.api`


## Подключение `jupiter`

```bash 

dc exec web /bin/sh 
apk add gcc python3-dev
pip install django-extensions jupyter

```

- Добавляем в `app.app.settings`: 

```python 

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888']
```