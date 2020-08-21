import pytest
from unittest.mock import MagicMock, patch
from Networking.UDPPinger.UDPClient import UDPClient
from socket import AF_INET, SOCK_DGRAM


SOCKET_STR = "socket.socket"


@pytest.fixture(scope="function")
def mock_client_socket():
    client_socket = MagicMock()
    client_socket.settimeout = MagicMock(side_effect=None)
    client_socket.gettimeout = MagicMock(return_value=3)
    return client_socket


@pytest.fixture(scope="function")
def mock_udp_client(mock_client_socket):
    with patch(SOCKET_STR, return_value=mock_client_socket) as mock_socket:
        client = UDPClient(3)
    mock_socket.assert_called_once_with(AF_INET, SOCK_DGRAM)
    mock_client_socket.settimeout.assert_called_once_with(3)
    return client


def test_instantiation(mock_udp_client, mock_client_socket):
    assert mock_udp_client.get_socket_timeout() == 3
    mock_client_socket.gettimeout.assert_called_once()
