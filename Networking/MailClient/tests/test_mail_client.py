import pytest
from unittest.mock import MagicMock, patch
from Networking.MailClient.mail_client import MailClient
from socket import AF_INET, SOCK_STREAM
from Networking.Base import exceptions as exc


SOCKET_STR = "socket.socket"
VALIDATE_STR = "Networking.MailClient.utils.print_and_validate_reply"


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


def test_receive_and_validate_no_exception(mock_mail_client,
                                           mock_client_socket):
    mock_client_socket.recv = MagicMock(return_value=b'250 Hello Matt.')
    with patch(VALIDATE_STR, side_effect=None) as mock_validate:
        mock_mail_client.receive_and_validate_reply(1024, 250)
    mock_client_socket.recv.assert_called_once_with(1024)
    mock_validate.assert_called_once_with('250 Hello Matt.', 250)


@patch(VALIDATE_STR, side_effect=exc.UnexpectedResponseCode(530, 250))
def test_receive_and_validate_with_exception(mock_validate, mock_mail_client,
                                             mock_client_socket):
    mock_client_socket.recv = MagicMock(
        return_value=b'530 Could not authenticate.')
    with pytest.raises(exc.UnexpectedResponseCode):
        mock_mail_client.receive_and_validate_reply(2048, 250)
    mock_client_socket.recv.assert_called_once_with(2048)
    mock_validate.assert_called_once_with('530 Could not authenticate.', 250)


def test_connect_and_validate_connection_success(mock_mail_client,
                                                 mock_client_socket):
    mock_mail_client.connect = MagicMock(side_effect=None)
    mock_mail_client.receive_and_validate_reply = MagicMock(side_effect=None)
    mock_mail_client._is_connected = True
    mock_mail_client.connect_and_validate_connection()
    mock_mail_client.connect.assert_called_once()
    mock_mail_client.receive_and_validate_reply.assert_called_once_with(
        1024, 220)
    assert mock_mail_client.is_connected()


def test_connect_and_validate_connection_failure(mock_mail_client,
                                                 mock_client_socket):
    mock_mail_client.connect = MagicMock(side_effect=None)
    mock_mail_client.receive_and_validate_reply = MagicMock(
        side_effect=exc.UnexpectedResponseCode(530, 220))
    mock_mail_client._is_connected = True
    mock_mail_client.connect_and_validate_connection()
    mock_mail_client.connect.assert_called_once()
    mock_mail_client.receive_and_validate_reply.assert_called_once_with(
        1024, 220)
    assert not mock_mail_client.is_connected()
