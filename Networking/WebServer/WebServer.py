import socket
from Networking.WebServer import utils

class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.running = False
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def is_running(self):
        return self.running

    def run(self):
        self.running = True
        while self.is_running():
            print("Ready to serve ...")
            connection_socket, addr = self.server_socket.accept()
            utils.render_page(connection_socket)


    def close(self):
        self.server_socket.close()
