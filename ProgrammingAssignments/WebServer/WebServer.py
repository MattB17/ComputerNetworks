import socket
from utils import read_message

class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def close(self):
        self.server_socket.close()

    def run(self):
        while True:
            print("Ready to serve ...")
            connection_socket, addr = self.server_socket.accept()
            try:
                message = connection_socket.recv(1024).decode()
                output_data = read_message(message)
                connection_socket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
                for i in range(0, len(output_data)):
                    connection_socket.send(output_data[i].encode())
                connection_socket.send("\r\n".encode())
            except IOError:
                connection_socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            finally:
                connection_socket.close()
