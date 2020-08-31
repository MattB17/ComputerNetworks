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

    def get_host(self):
        """The host to which the client connects.

        Returns
        -------
        str
            A string representing the host to which the client connects.

        """
        return self._host

    def get_port(self):
        """The port to which the client connects.

        Returns
        -------
        int
            An integer representing the port to which the client connects.

        """
        return self._port

    def get_email_address(self):
        """The email address associated with the client.

        Returns
        -------
        str
            A string representing the client's email address.

        """
        return self._email

    def connect(self):
        """Connects the client to the email server.

        Returns
        -------
        None

        """
        self._client_socket.connect((self._host, self._port))
        self._is_connected = True

    def is_connected(self):
        """Indicates if the client is connected to the email server.

        Returns
        -------
        bool
            True if the client is connected to the email server.
            Otherwise, False.

        """
        return self._is_connected

    def disconnect(self):
        """Disconnects the client from the email server.

        Returns
        -------
        None

        """
        self._client_socket.close()
        self._is_connected = False
