"""The WebServer class is used to run a web server.

"""
import socket
from Networking.WebServer import utils


class WebServer:
    def __init__(self, host, port):
        """Encapsulates the functionality of a web server.

        Parameters
        ----------
        host: str
            A string representing the host on which the server is run.
        port: int
            An integer representing the port number where the server is run.

        Attributes
        ----------
        _host: str
            The host on which the server runs.
        _port: int
            The port on which the server runs.
        _running: bool
            Specifies whether the server is currently running.
        _server_socket: socket.socket
            The socket used to run the server.

        """
        self._host = host
        self._port = port
        self._running = False
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((host, port))
        self._server_socket.listen(1)

    def get_host(self):
        """The host for the web server.

        Returns
        -------
        str
            A string identifying the host running the server.

        """
        return self._host

    def get_port(self):
        """The port number for the web server.

        Returns
        -------
        int
            An integer identifying the port number for the server.

        """
        return self._port

    def is_running(self):
        """Specifies whether the server is currently running.

        Returns
        -------
        bool
            True if the server is currently running. Otherwise, False.

        """
        return self._running

    def run(self):
        """Runs the web server.

        Returns
        -------
        None

        """
        self._running = True
        while self.is_running():
            print("Ready to serve ...")
            connection_socket, addr = self._server_socket.accept()
            utils.render_page(connection_socket)


    def close(self):
        """Closes the socket associated with the server.

        Returns
        -------
        None

        """
        self._server_socket.close()
