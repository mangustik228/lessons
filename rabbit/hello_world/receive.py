import os
import sys
import pika


def callback(ch, method, properties, body):
    print(f'{type(ch) = }')
    print(f'{type(method) = }')
    print(f'{type(properties) = }')
    print(f'{type(body) = }')
    print(f"Received message {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_consume(
    queue="hello",
    auto_ack=True,
    on_message_callback=callback
)


def main():
    print(" Waiting msgs. To exit press CTRL+C")
    channel.basic_publish(
        exchange="", routing_key="hello", body="FIRST MESSAGE")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit")
        try:
            sys.exit()
        except SystemError:
            os._exit(0)


channel.close()
connection.close()
