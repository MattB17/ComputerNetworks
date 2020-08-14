"""The NetworkServer class is a generic server class from which other server
classes inherit. It provides the base functionality needed for a server
on which inheriting classes can build.

"""
import socket


class NetworkServer:
    """Encapsulates the generic functionality of a server.

    Parameters
    ----------
    host: str
        A string representing the host on which the server is run.
    port: int
        A string representing the port on which the server is run.
    family: AddressFamily
        The socket family used for the server's socket
    type: SocketKind
        The socket type used for the server's socket

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
    def __init__(self, host, port, family, type):
        self._host = host
        self._port = port
        self._running = False
        self._server_socket = socket.socket(family, type)
        self._server_socket.bind((host, port))

    def get_host(self):
        """The host for the server.

        Returns
        -------
        str
            A string identifying the host running the server.

        """
        return self._host

    def get_port(self):
        """The port number for the server.

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
        """Runs the server.

        Returns
        -------
        None

        """
        self._running = True

    def stop(self):
        """Stops the server from running.

        Returns
        -------
        None

        """
        self._running = False
