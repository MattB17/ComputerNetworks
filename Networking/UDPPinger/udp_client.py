"""The UDPClient class implements a client using the UDP Protocol.

"""
import socket
import datetime
from Networking.UDPPinger import utils


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
            The port at which the message is received.

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

    def send_ping_wait_for_response(self, ping_number, dest_host,
                                    dest_port, recv_port):
        """Sends a ping message with `ping_number` and waits for a response.

        The message is sent to the node identified by `dest_host` and
        `dest_port` and the socket waits for a response at `recv_port`. If
        the socket times out a message is printed to the console indicating
        that this is the case. Otherwise, the received message and round trip
        time are printed to the console.

        Parameters
        ----------
        ping_number: int
            The number specified in the ping message.
        dest_host: str
            A string representing the host to which the message is sent.
        dest_port: int
            An integer representing the port to which the message is sent.
        recv_port: int
            The port at which the reply message is received.

        Returns
        -------
        None

        """
        self.send_ping(ping_number, dest_host, dest_port)
        try:
            reply_message = self.receive_and_decode_message(recv_port)
            reply_time = datetime.now()
            print(reply_message)
            print("RTT of {} ms\n".format(
                utils.get_rtt_from_pong_message(reply_message, reply_time)))
        except socket.timeout:
            print("Request timed out\n")

    def send_ping_sequence(self, num_pings, dest_host, dest_port, recv_port):
        """Sends a sequence of ping messages to `dest_host` at `dest_port`.

        A series of `num_pings` ping messages are constructed and sent to the
        node identified by `dest_host` and `dest_port`. After sending each
        ping, the client waits for a pong (response message) and prints the
        message as well as the round trip time. If the socket times out
        waiting for a response then a message is printed indicating this case.

        Parameters
        ----------
        num_pings: int
            The number of ping messages to be sent.
        dest_host: str
            A string representing the host to which the pings are sent.
        dest_port: int
            An integer representing the port to which the pings are sent.
        recv_port: int
            The port at which the pongs are received.

        Raises
        ------
        InvalidPingCount
            If `num_pings` does not represent a valid number of ping messages
            to send.

        Returns
        -------
        None

        """
        utils.validate_ping_count(num_pings)
        for i in range(num_pings):
            self.send_ping_wait_for_response(
                i, dest_host, dest_port, recv_port)
