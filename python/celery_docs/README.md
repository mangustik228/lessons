
### redis 

```bash 

docker run -d -p 6379:6379 redis

# redis-cli 
docker exec -it [id_container] redis-cli 

# get all tasks (redis-cli)
LRANGE celery 0 -1

# clear redis
docker exec -it 30c5e6555f2f redis-cli FLUSHALL

```

### consumer 

```bash 
# Запуск worker
celery -A consumer_file worker --loglevel=INFO

```

