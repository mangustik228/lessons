'''
Создание событийного цикла на selectors. 
'''
import selectors
import socket

# Вернет дефолтный селектор для моей os
selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()
    selector.register(
        fileobj=server_socket,  # Что отслеживаем
        events=selectors.EVENT_READ,  # Какой объект отслеживаем
        data=accept_connection,  # Любые связанные данные с этим отслеживанием
    )


def accept_connection(server_socket: socket.socket):
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_socket: socket.socket):
    request = client_socket.recv(1024)

    if request:
        txt = request.decode("utf-8")
        response = f"your message: {txt}\n".encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)  # Снимаем с регистрации
        client_socket.close()


def event_loop():
    while True:
        # Возвращает кортеж (key: SelectorKey, events)
        # SelectorKey - именнованный кортеж.
        # fileobj
        # events
        # data
        events = selector.select()
        for key, _ in events:
            callback: callable = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
