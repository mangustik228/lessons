## lessons: [udemy](https://www.youtube.com/playlist?list=PLBxwSeQlMDNjT6SuPn4PAviXhGNsvkpsZ)




**`.vscode/launch.json`**

```bash 
    # need to change
    "program": "${workspaceFolder}/manage.py",
    # to
    "program": "${workspaceFolder}/onlinestore/manage.py",


    # need to comment: 
    // "--nothreading"
```



Объявляение models в `app/some_service/models.py` 

Объявление views `app/some_service/views.py`

Объявление templates `app/some_service/templates/some_service/product_detail.html`

Добавляем классы в `app/some_service/urls.py` 

Добавляем пути в `app/app/urls.py` (Тут же добавляеться статика)

Добавляем в `app/app/settings.py` MEDIA_URL & MEDIA_ROOT

Регистрируем модели в Админ-панели: `app/some_service/admin.py`


## DRF 

```bash 
pip install djangorestframework
```

Добавляем в `app/app/settings/INSTALLED_APPS`: rest_framework