'''
Создание простого событийного цикла. 
'''
import socket
from select import select

# select - системная ф-ция для мониторинга изменений состояния файловых объектов и сокетов.
# Принимает списки объектов:
# rlist - read list (те объекты за которыми следить, когда будут доступны для чтения)
# wlist - write list (те объекты за которыми следить, когда будут доступны для записи)
# xlist - ...
# возвращает теже объекты

to_monitoring = []  # список объектов которые нужно мониторить


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5000))
server_socket.listen()


def accept_connection(server_socket: socket.socket):
    '''Принимает серверный сокет'''
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")
    to_monitoring.append(client_socket)


def send_message(client_socket: socket.socket):
    '''Принимает клиентский сокет'''
    request = client_socket.recv(1024)

    if request:
        txt = request.decode("utf-8")
        response = f"your message: {txt}\n".encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop(to_monitoring: list[socket.socket]):
    while True:
        ready_read, _, _ = select(to_monitoring, [], [])
        # ready_read - список сокетов
        for sock in ready_read:
            if sock is server_socket:
                accept_connection(sock)
            else:  # sock is client
                send_message(sock)


if __name__ == '__main__':
    to_monitoring.append(server_socket)
    event_loop(to_monitoring)
