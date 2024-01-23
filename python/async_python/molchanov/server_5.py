'''
Асинхронность на генераторах по принципу "Round Robbin"
# David Beazley 
# 2015 PyCon 
# Concurrency from the Ground up Live 
'''


import socket
from select import select
from typing import Any, Generator

tasks: list[Generator] = []
to_read: dict[socket.socket, Generator] = {}
to_write: dict[socket.socket, Generator] = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    while True:
        yield "read", server_socket
        client_socket, addr = server_socket.accept()  # read
        tasks.append(client(client_socket))
        print(f"Connection from {addr}")


def client(client_socket: socket.socket):
    while True:

        yield "read", client_socket
        request = client_socket.recv(1024)  # read

        if not request:
            break

        txt = request.decode("utf-8")
        response = f"your message: {txt}\n".encode()

        yield "write", client_socket
        client_socket.send(response)  # write

    print("connection close")
    client_socket.close()


def event_loop():
    while True:

        while not tasks:
            # Получаем готовые сокеты.
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
                # (generator)

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == "read":
                to_read[sock] = task
                # { socket : ('read', socket) }
            if reason == "write":
                to_write[sock] = task
        except StopIteration:
            print("done!")


if __name__ == '__main__':
    tasks.append(server())
    event_loop()
