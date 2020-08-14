import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12000))

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)
    message = message.decode().upper()
    message_lst = message.split()
    message_lst[0] = "PONG"
    message = " ".join(message_lst)
    if rand >= 4:
        server_socket.sendto(message.encode(), address)
