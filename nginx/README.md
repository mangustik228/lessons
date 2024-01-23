# Мини курс с [ютуб](https://www.youtube.com/watch?v=b8ObIf1YR18&list=PLhgRAQ8BwWFa7ulOkX0qi5UfVizGD_-Rc&index=2)

## About Nginx

Nginx - reverse proxy 

## Nginx vs Apache 

apache - prefork (запускает кучу процессов, каждый обрабатывает n запросов в единицу времени)
nginx - обрабатывает запросы асинхронно (несколько запросов одновременно), в отличии от apache не может встраивать серверные языки в свои процессы. А главное может выдавать статический контент без использования серверного языка

Использование ресурсов - менее прожорливый. 

**EXAMPLE:**
```nginx 

server {
    listen 80;
    server_name mysite.com;

    root /example/site/http;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }
}

```

### INSRALL 

#### Easy way 

```bash 
# ubuntu 
sudo apt install nginx 

# Файлы конфигурации nginx 
ls -l /etc/nginx/

```

#### Hard way (из исходники)

```bash 
wget [link_to_off_nginx] # Скачать 
tar -zxvf nginx... # Разархивировать
cd nginx-1.... # Перейти в директорию
sudo apt install libpcre3 libpcre3-dev libpcrecpp0 libssl-dev zlib1g-dev
# Посмотреть флаги: https://www.nginx.com/resources/wiki/start/topics/tutorials/installoptions/
# --sbin-path=/usr/bin/nginx Как установим исполняемые файлы nginx 
# --conf-path=/etc/nginx/nginx.conf Куда устанавливаем файлы конфигурации 
# --error-log-path=/val/log/nginx/error.log Где храним ошибочные логи
# --http-log-path=/var/log/nginx/access.log Где нормальные логи с отладкой. МОЖНО ДОБАВИТЬ --with-debug
# --with-pcre Можно использовать какие то выражения
# --with-zlib=../zlib-1.1.3 
./configure --sbin-path=/usr/bin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/val/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-pcre=../pcre-4.4 --with-zlib=../zlib-1.1.3 --with-http_ssl_module
# Преимущества установки из исходника: 
# Возможность указать модули, например 
# --with-http_ssl_module
# Все модули можно посмотреть тут: https://www.nginx.com/resources/wiki/modules/
``` 

### Добавляем NGINX в сервисы

Надо добавить сервис nginx(Если собирали сами).  
См.документацию: https://www.nginx.com/resources/wiki/start/topics/examples/initscripts/
Скачиваем в cd /etc/init.d/

```bash 
cd /etc/init.d # Переходим в /etc/init.d - тут храняться файлы службы
wget LINK # Копируем нужный скрипт 
sudo chmod +x nginx # Делаем скрипт исполняемым
update-rc.d -f nginx defaults # Добавляем nginx в сервисы
echo "NGINX_CONF_FILE=/etc/nginx/nginx.conf" > /etc/default/nginx # Указываем откуда грузить конфиг nginx
echo DAEMON=/user/bin/nginx >> etc/default/nginx 
sudo service nginx status 
``` 


### Термины в натсройках NGINX 

Контекст 
Директивы 


```bash 
worker_processes 1; # Директива для мастер-контекста


# Вместе - контекст (фактически зона видимости)
events {
    worker_connections 1024; # Опция + значение опции, а вместе - директива
}

```

## First start 

Удаляем из контекста все из контекста html и контекста events

```nginx.conf 

events {}

http {
    
    inclue mime.types # Подключение поддерживаемых типов     

    server {
        listen 80; # Что слушаем 
        server_name; 176.9.36.99 # Сервер
        root /home/vovchinnikov/www # Путь
    }
}
``` 

## Location 

Модификаторы: 

```bash 
location /greet {...} # /greeting /greete - все сработает 
location = /greet {...} # Полное сравнение 
location ~ /gree[0-9] {...} # Совпадение по регулярному выражению. Чувствителен к регистру 
location *~ /gree[0-9] {...} # Совпадение по регулярному выражению. Не чувствителен к регистру
location ^~ /greet {...} # Аналог регулярке, но выше приооритет
```

Порядок совпадений используемый в NGINX:

```bash 
= # Полное совпадение 
^~ # Префикс преимущества 
~&*~ # Регулярное выражение
# Без модификатора


```nginx.conf

http {
    ... 
    server {
        ... 
        location /gree {
            return 200 'Hello from nginx location block'
        }
    }
}
```

### Логгирование 

Логи ошибок - /var/logs/nginx/errors.log 
Логи подключений - /var/logs/nginx/access.log 
Также можно подключить дополнительно ошибки и `location`:
также можно отключить логи

```bash 
http {
    ... 
    server {
        ... 
        location /example {
            error_log /var/log/nginx/example.error.log debug;
            access_log off;  
            ... 
        }
    }
}
``` 

### Наследование директив 

Например директива 

http {
    gzip on; # Будет наследоваться у всех, можно переопределить
}

http -> server -> location

Директивы действия rewrite / return . Вообще не наследуется

#### Директива try_files (Особое поведение)

location /downloads {
    ... 
    try_files $uri =404; # Пытается получиться файл - если не найдет, вернут 404 ошибку
    try_file $uri index.html =404 # Сначало попытается прогрузить index.html а потом уже 404 ошибка 
}


## Работа с серверными языками   
### PHP
```bash 
sudo apt install php{version}_fpm 
sudo apt install php{version}_mysql
sudo apt install php{version}_cgi
```


### Основные конфигурации 

```bash

load_module "modules/..."; # Подключение модуля

user www-data www-data; 

worker_process auto; # Сколько можно запустить экземпляров. не более 1 процесса на 1 ядро 

events {
    # Сколько запросов может одновременно обрабатывать 1 worker. Или сколько запросов может выполнить параллельно процессор
    worker_connections 1024; 

    # Позволяет принимать неограниченное кол-во подключений, если off - то только одно подключение за ед. времени
    multi_accept on; 
    
    use epoll; 
}

http { 
    # Кодировка по умолчанию
    charset utf-8;  

    # Всякое связанное с кэш. 
    open_file_cache max=1000 inactive=20s; 

    # Через сколько закроется соединение в ms
    keepalive_timeout 300;

    # Максимальное кол-во времени через сколько соединение будет закрыто 
    send_timeout 10; 

    # Стандартные Mime Types 
    include /etc/nginx/mime.types; 

    # Add extra mime types
    types {
        application/x-httpd-php .html;
    }

    server {
        ... 
        # Добавить заголовок в ответ
        add_header "Cache-Control" "no-transform";

        # IFrame будут работать только если с того же домена 
        add_header X-Frame-Options SAMEORIGIN;
    }
}

```

### Заголовки Expires (Когда понадобиться - читай про кеш на стороне клиента)

```bash 
location /example.com {
    expires 1M;
}
``` 

### Заголовок gzip 

```bash

http {
    server {
        ... 
        #GZIP Configuration 
        gzip on; 
        # Файл менее 100 байт не будет сжат
        gzip_min_length 100; 
        # Чем больше число - тем сильнее сжатие, но и больше процессорного времени. правильнее использовать 2-4
        gzip_comp_level 3; 
        # Что сжимаем 
        gzip_types text/plain;
        gzip_types text/css;
        gzip_types text/javascript;

        # Проверяет заголовок клиента и если в user-agent есть этот заголовок, то отключает
        gzip_disable "msie6";
    }
}

```

### Не много о безопасности 

```bash 
http {
    ... 
    server_tokens off; # отключаем информацию о версии nginx 


    # Добавляем размеры буферов (Существует атака "переполнение буфера")
    client_body_buffer_size 16k;
    client_header_buffer_size 1k;
    client_max_body_size 8m; 
    large_client_header_buffers 2 1k; 

    # Block User Agents 
    if ($http_user_agent ~* Mozilla) {
        return 403;
    }

    if ($http_referer ~* ... ) {
        return 403; # Работает такжже как $http_user_agent
    }

    # Только наши IFrame 
    add_header X-Frame-Options SAMEORIGIN;
}

```


### LETS ENCRYPT 

### Обратный прокси-сервер 

```bash 

http {
    server {
        ...
        
        location /php {
            ...
            proxy_pass http://localhost:9999/;
        }

        location /nginxorg {
            proxy_pass 'https://nginx.org/'
        }
    }
}

```


### Балансировка нагрузки 

```bash
{
    http {
        upstream my_servers {
            server localhost:10001;
            server localhost:10002;
            server localhost:10003;
        }
    }

    server {
        listen 80; 
        location / {
            proxy_pass http://my_servers; 
        }
    }
}

```

По умолчанию используется - round robin 

можно добавить в контекст upstream дериктивы: 
- ip_hash; # Проксировать для одного ip на один и тот же сервис (Если доступен)
- least_conn; # Наименьшее кол-во подключений