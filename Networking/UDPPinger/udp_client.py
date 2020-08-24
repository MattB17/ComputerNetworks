"""The UDPClient class implements a client using the UDP Protocol.

"""
import socket
import datetime


class UDPClient:
    """Implements a UDP Client that waits `timeout` seconds for responses.

    Parameters
    ----------
    timeout: int
        The number of seconds that the client waits for a response to a
        message it has sent.

    Attributes
    ----------
    _client_socket: socket.socket
        The socket that the client interacts with.

    """
    def __init__(self, timeout):
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._client_socket.settimeout(timeout)

    def get_socket_timeout(self):
        """Retrieves the timeout set on the client's socket.

        Returns
        -------
        int
            An integer corresponding to the number of seconds that the
            client's socket waits for a response.

        """
        return self._client_socket.gettimeout()

    def send_ping(self, ping_number, dest_host, dest_port):
        """Sends a ping message with number `ping_number` to `dest_host`.

        Parameters
        ----------
        ping_number: int
            The ping number to be sent in the message.
        dest_host: str
            A string representing the host to which the message is sent.
        dest_port: int
            An integer representing the port to which the message is sent.

        Returns
        -------
        None

        """
        message = "ping {0} {1}".format(ping_number, datetime.now())
        self._client_socket.sendto(message.encode(), (dest_host, dest_port))

    def receive_and_decode_message(self, recv_port):
        """Receives a message on `recv_port` and decodes the message.

        Parameters
        ----------
        recv_port: int
            The port at which the message is received on.

        Raises
        ------
        socket.timeout
            If the socket times out waiting for a message.

        Returns
        -------
        str
            A string representing the decoded message received on `recv_port`.

        """
        received_message, from_addr = self._client_socket.recvfrom(recv_port)
        return received_message.decode()
