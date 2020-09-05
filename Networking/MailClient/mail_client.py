"""The MailClient class is used to run an email client using the SMTP
protocol.

"""
import socket
import ssl
from Networking.MailClient import utils
from Networking.Base import exceptions as exc

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
    _connection_secured: bool
        A boolean indicating if a secure connection has been established.

    """
    def __init__(self, host, port, email):
        self._client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port
        self._email = email
        self._is_connected = False
        self._connection_secured = False

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

    def receive_and_validate_reply(self, recv_bytes, expected_code):
        """Receives and validates a reply message from the server.

        The received message is validated using `expected_code`.

        Parameters
        ----------
        recv_bytes: int
            An integer representing the maximum number of bytes that can be
            received.

        Raises
        ------
        UnexpectedResponseCode
            If the received reply contains a code other than `expected_code`.

        Returns
        -------
        None

        Side Effect
        -----------
        The received reply is printed to the console.

        """
        reply_msg = self._client_socket.recv(recv_bytes).decode()
        utils.print_and_validate_reply(reply_msg, expected_code)

    def connect_and_validate_connection(self):
        """Requests connection to the server and validates the connection.

        Returns
        -------
        None

        """
        self.connect()
        try:
            self.receive_and_validate_reply(1024, 220)
        except:
            self._is_connected = False

    def is_connection_secure(self):
        """Indicates if the client has a secure connection to the server.

        Raises
        ------
        ConnectionNotEstablished
            If a connection to the mail server has not been established.

        Returns
        -------
        bool
            True if the client has a secure connection to the server.
            Otherwise, False.

        """
        if not self.is_connected():
            raise exc.ConnectionNotEstablished(self._host, self._port)
        return self._connection_secured

    def secure_connection(self):
        """Secures an existing connection to the mail server.

        Raises
        ------
        ConnectionNotEstablished
            If a connection to the mail server has not been established. In
            this case there is no connection to secure.

        Returns
        -------
        None

        Side Effect
        -----------
        Secures the client socket converting from an instance of
        `socket.socket` to an instance of `ssl.SSLSocket` which is a derived
        class of `socket.socket`.

        """
        if not self.is_connection_secure():
            context = ssl.create_default_context()
            self._client_socket = context.wrap_socket(
                self._client_socket, server_hostname=self._host)
            self._connection_secured = True

    def create_secure_connection(self):
        """Creates a new secure connection to the mail server.

        A new connection is created to the mail server and secured with SSL.
        If a secure connection already exists, nothing is done. If an unsecure
        connection exists, this connection is secured.

        Returns
        -------
        None

        Side Effect
        -----------
        creates a secure connection from the client to the server.

        """
        if not self.is_connected():
            self.connect()
        self.secure_connection()

    def unsecure_connection(self):
        """Unsecures an existing secure connection to the mail server.

        Raises
        ------
        ConnectionNotEstablished
            If the client is currently not connected to the mail server.
        ConnectionNotSecure
            If there is an existing connection that is not currently secure.
            The user is alerted in this case as he/she may have inadvertently
            sent sensitive information over an unencrypted channel.

        Returns
        -------
        None

        """
        if not self.is_connection_secure():
            raise exc.ConnectionNotSecure(self._host, self._port)
        self._client_socket = self._client_socket.unwrap()
