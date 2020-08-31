import pytest
from unittest.mock import MagicMock, patch
from Networking.MailClient.mail_client import MailClient
from socket import AF_INET, SOCK_STREAM


SOCKET_STR = "socket.socket"


@pytest.fixture(scope="function")
def mock_client_socket():
    socket = MagicMock()
    socket.connect = MagicMock(side_effect=None)
    socket.close = MagicMock(side_effect=None)
    return socket


@pytest.fixture(scope="function")
def mock_mail_client(mock_client_socket):
    with patch(SOCKET_STR, return_value=mock_client_socket) as mock_socket:
        client = MailClient('127.0.0.1', 8080, "some.email@address.com")
    mock_socket.assert_called_once_with(AF_INET, SOCK_STREAM)
    return client


def test_instantiation(mock_mail_client):
    assert mock_mail_client.get_host() == '127.0.0.1'
    assert mock_mail_client.get_port() == 8080
    assert mock_mail_client.get_email_address() == "some.email@address.com"
    assert not mock_mail_client.is_connected()


def test_connecting(mock_mail_client, mock_client_socket):
    assert not mock_mail_client.is_connected()
    mock_mail_client.connect()
    mock_client_socket.connect.assert_called_once_with(('127.0.0.1', 8080))
    assert mock_mail_client.is_connected()


def test_disconnecting(mock_mail_client, mock_client_socket):
    mock_mail_client._is_connected = True
    assert mock_mail_client.is_connected()
    mock_mail_client.disconnect()
    mock_client_socket.close.assert_called_once()
    assert not mock_mail_client.is_connected()
