Запуск кролика: 

```bash
docker run -d --name rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
docker stop rabbit
docker rm rabbit
docker exec rabbit rabbitmqctl list_queues
```