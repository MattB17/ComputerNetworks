import pytest
from unittest.mock import MagicMock, patch, call
from Networking.UDPPinger.UDPServer import UDPServer
from Networking.Base.NetworkServer import NetworkServer
from socket import AF_INET, SOCK_DGRAM


SOCKET_STR = "socket.socket"


@pytest.fixture(scope="function")
def mock_server_socket():
    server_socket = MagicMock()
    server_socket.bind = MagicMock(side_effect=None)
    server_socket.close = MagicMock(side_effect=None)
    return server_socket


@pytest.fixture(scope="function")
def mostly_reliable_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket):
        server = UDPServer('127.0.0.1', 8080, 0.7)
    return server


def test_correct_inheritance():
    assert issubclass(UDPServer, NetworkServer)


def test_instantiation(mostly_reliable_server):
    assert mostly_reliable_server.get_host() == '127.0.0.1'
    assert mostly_reliable_server.get_port() == 8080
    assert not mostly_reliable_server.is_running()
    assert mostly_reliable_server.get_reliability() == 0.7
