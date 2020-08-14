import socket
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

server_name = '127.0.0.1'
server_port = 12000

for i in range(10):
    message = "Ping {0} {1}".format(i+1, datetime.now())
    client_socket.sendto(message.encode(), (server_name, server_port))
    try:
        modified_message, server_address = client_socket.recvfrom(1024)
        modified_message = modified_message.decode()
        print(modified_message)
        sent_time_str = " ".join(modified_message.split()[2:])
        sent_time = datetime.strptime(sent_time_str, "%Y-%m-%d %H:%M:%S.%f")
        rtt = int(str(datetime.now() - sent_time).split(".")[1])
        print("RTT of {} ms".format(rtt))
    except socket.timeout:
        print("Request timed out")
    if i < 9:
        print("------------------")
