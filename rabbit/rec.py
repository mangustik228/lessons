import redis

# Подключение к Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Получение и обработка сообщения из хэша
message = redis_client.hgetall("notifications")
print("Получено уведомление:")
print("Заголовок:", message[b'title'].decode('utf-8'))
print("Содержание:", message[b'content'].decode('utf-8'))
