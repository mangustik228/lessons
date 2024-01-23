import socket

# Открываем socket
server_socket = socket.socket(
    socket.AF_INET,  # IPv4 (address family)
    socket.SOCK_STREAM  # support TCP (protocol)
)

# Переоткрыть порт
server_socket.setsockopt(
    socket.SOL_SOCKET,  # Опция к уровню сокета...
    socket.SO_REUSEADDR,  # Какую опцию установить
    1  # Какое значение
)

# Привязываем к порту
server_socket.bind(("localhost", 5000))

# Прослушиваем
server_socket.listen()

while True:
    print("before accept. wait connection")
    # accept - читает данные из входящего буфера и если что то пришло, то возвращает кортеж.
    client_socket, addr = server_socket.accept()
    print("connection from", addr)

    while True:
        # Принимает какое сообщение от пользователя. 4096 - размер буфера
        print("before .recv()")
        request = client_socket.recv(1024)

        if not request:
            break
        else:
            response = "hello world\n".encode()
            client_socket.send(response)
    print("outside innser while loop")
    client_socket.close()
