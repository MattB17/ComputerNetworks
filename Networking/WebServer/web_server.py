"""The WebServer class is used to run a web server.

"""
import socket
from Networking.WebServer import utils
from Networking.Base.network_server import NetworkServer


class WebServer(NetworkServer):
    """Encapsulates the functionality of a web server.

    WebServer is a derived class of the generic `NetworkServer`.

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
    def __init__(self, host, port):
        super().__init__(host, port, socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.listen(1)

    def run(self):
        """Runs the web server.

        Returns
        -------
        None

        """
        super().run()
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
        super().stop()
        self._server_socket.close()
