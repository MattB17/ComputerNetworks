import pytest
from unittest.mock import MagicMock, patch
from Networking.Base.network_server import NetworkServer
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM


SOCKET_STR = "socket.socket"


@pytest.fixture(scope="function")
def mock_server_socket():
    server_socket = MagicMock()
    server_socket.bind = MagicMock(side_effect=None)
    return server_socket


@pytest.fixture(scope="function")
def mock_stream_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket) as mock_socket:
        server = NetworkServer('127.0.0.1', 8080, AF_INET, SOCK_STREAM)
    mock_socket.assert_called_once_with(AF_INET, SOCK_STREAM)
    mock_server_socket.bind.assert_called_once_with(('127.0.0.1', 8080))
    return server


@pytest.fixture(scope="function")
def mock_dgram_server(mock_server_socket):
    with patch(SOCKET_STR, return_value=mock_server_socket) as mock_socket:
        server = NetworkServer('localhost', 6590, AF_INET, SOCK_DGRAM)
    mock_socket.assert_called_once_with(AF_INET, SOCK_DGRAM)
    mock_server_socket.bind.assert_called_once_with(('localhost', 6590))
    return server


def test_instantiation_stream(mock_stream_server):
    assert mock_stream_server.get_host() == '127.0.0.1'
    assert mock_stream_server.get_port() == 8080
    assert not mock_stream_server.is_running()


def test_instantiation_dgram(mock_dgram_server):
    assert mock_dgram_server.get_host() == 'localhost'
    assert mock_dgram_server.get_port() == 6590
    assert not mock_dgram_server.is_running()


def test_run(mock_stream_server):
    assert not mock_stream_server.is_running()
    mock_stream_server.run()
    assert mock_stream_server.is_running()


def test_stop(mock_dgram_server):
    mock_dgram_server.run()
    assert mock_dgram_server.is_running()
    mock_dgram_server.stop()
    assert not mock_dgram_server.is_running()
