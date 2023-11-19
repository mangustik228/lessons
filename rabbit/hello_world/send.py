import pika
import sys

# Создание подключения
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
# Создание очереди
channel.queue_declare(queue="hello")


channel.basic_publish(
    exchange="",  # Обменник... ?!
    routing_key="hello",  # Имя очереди
    body=f"hello world {sys.argv[1]}"  # Сообщение
)


channel.close()
connection.close()
