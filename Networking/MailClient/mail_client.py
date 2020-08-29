"""The MailClient class is used to run an email client using the SMTP
protocol.

"""
import socket

class MailClient:
    """Encapsulates the functionality of a mail client.

    Parameters
    ----------
    host: str
        The host to which the client connects.
    port: int
        The port to which the client connects.
    email: str
        The email address associated with the client.

    Attributes
    ----------
    _client_socket: socket.socket
        The socket through which the client interacts with the server.
    _host: str
        The host to which the client connects.
    _port: int
        The port to which the client connects.
    _email: str
        The email address associated with the client.
    _is_connected: bool
        A boolean indicating if the client is connected to the host.

    """
    def __init__(self, host, port, email):
        self._client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port
        self._email = email
        self._is_connected = False
