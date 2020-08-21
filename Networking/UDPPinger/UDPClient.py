"""The UDPClient class implements a client using the UDP Protocol.

"""
import socket


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
