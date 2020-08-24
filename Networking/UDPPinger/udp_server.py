"""The UDPServer class implements a server using the UDP protocol.

"""
import socket
from Networking.Base.NetworkServer import NetworkServer
from Networking.UDPPinger import utils


class UDPServer(NetworkServer):
    """Implements a UDP Server of a given `reliability`.

    UDPServer is a dervived class of the generic NetworkServer.

    Parameters
    ----------
    host: str
        A string representing the host on which the server is run.
    port: int
        An integer representing the host on which the server is run.
    reliability: float
        A float representing the reliability of the server. Values are
        between 0 and 1 giving the long run proportion of packets that
        are successfully received. That is, for a value of `x` the server
        will successfully receive `100x` percent of packets when running
        for a sufficiently long time.

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
    _reliability: float
        The server's reliability. A value between 0 and 1 representing
        the long run proportion of packets that are successfully received.

    """
    def __init__(self, host, port, reliability):
        utils.validate_proportion(reliability)
        super().__init__(host, port, socket.AF_INET, socket.SOCK_DGRAM)
        self._reliability = reliability

    def get_reliability(self):
        """Gives the reliability of the server.

        The reliability is a float between 0 and 1 representing the long run
        proportion of packets that are successfully received by the server.

        Returns
        -------
        float
            A float representing the server's reliability.

        """
        return self._reliability

    def run(self):
        """Runs the UDP server.

        While running, the server receives, processes, and replies to
        messages. Only a proportion of messages, equal to the server's
        reliability, are successfully processed.

        Returns
        -------
        None

        """
        super().run()
        while self.is_running():
            message, addr = self._server_socket.recvfrom(1024)
            if not utils.will_drop_message(self._reliability):
                self._server_socket.sendto(
                    utils.process_message(message.decode()).encode(), addr)
