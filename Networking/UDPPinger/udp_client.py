import socket
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

server_name = ''
server_port = 12000

for i in range(10):
    message = "Ping {0} {1}".format(i+1, datetime.now())
    client_socket.sendto(message, (server_name, server_port))
    try:
        modified_message, server_address = client_socket.recvfrom(1024)
        print(modified_message)
    except socket.timeout:
        print("Request timed out")
