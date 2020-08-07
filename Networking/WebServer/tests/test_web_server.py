import pytest
from unittest.mock import MagicMock, patch
from Networking.WebServer.WebServer import WebServer
from socket import AF_INET, SOCK_STREAM


SOCKET_STR = "Networking.WebServer.WebServer.socket.socket"


@pytest.fixture(scope="function")
def mock_server_socket():
    server_socket = MagicMock()
    server_socket.bind = MagicMock(side_effect=None)
    server_socket.listen = MagicMock(side_effect=None)
    server_socket.close = MagicMock(side_effect=None)
    return server_socket


@pytest.fixture(scope="function")
def mock_web_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket) as mock_socket:
        server = WebServer('127.0.0.1', 8000)
    mock_socket.assert_called_once_with(AF_INET, SOCK_STREAM)
    mock_server_socket.bind.assert_called_once_with(('127.0.0.1', 8000))
    mock_server_socket.listen.assert_called_once_with(1)
    return server


def test_instantiation(mock_web_server):
    assert mock_web_server.get_host() == '127.0.0.1'
    assert mock_web_server.get_port() == 8000
