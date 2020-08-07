import socket
from Networking.WebServer import utils

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

    def run(self):
        while True:
            print("Ready to serve ...")
            connection_socket, addr = self.server_socket.accept()
            try:
                message = connection_socket.recv(1024).decode()
                output_data = utils.read_message(message)
                utils.send_data_through_socket(connection_socket, output_data)
            except IOError:
                connection_socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            finally:
                connection_socket.close()


    def close(self):
        self.server_socket.close()
