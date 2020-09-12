import pytest
from unittest.mock import MagicMock, patch, call
from Networking.MailClient.mail_client import MailClient
from socket import AF_INET, SOCK_STREAM
from Networking.Base import exceptions as exc


SOCKET_STR = "socket.socket"
VALIDATE_STR = "Networking.MailClient.utils.print_and_validate_reply"
CONTEXT_STR = "ssl.create_default_context"
PASS_STR = "getpass.getpass"
BASE64_STR = "base64.b64encode"


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


@pytest.fixture(scope="function")
def mock_ssl_socket():
    return MagicMock()


@pytest.fixture(scope="function")
def mock_context(mock_ssl_socket):
    context = MagicMock()
    context.wrap_socket = MagicMock(return_value=mock_ssl_socket)
    return context


def test_instantiation(mock_mail_client):
    assert mock_mail_client.get_host() == '127.0.0.1'
    assert mock_mail_client.get_port() == 8080
    assert mock_mail_client.get_email_address() == "some.email@address.com"
    assert not mock_mail_client.is_connected()
    assert not mock_mail_client._connection_secured


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


def test_is_connection_secure_gives_false(mock_mail_client):
    mock_mail_client.is_connected = MagicMock(return_value=True)
    mock_mail_client._connection_secured = False
    assert not mock_mail_client.is_connection_secure()
    mock_mail_client.is_connected.assert_called_once()


def test_is_connection_secure_gives_true(mock_mail_client):
    mock_mail_client.is_connected = MagicMock(return_value=True)
    mock_mail_client._connection_secured = True
    assert mock_mail_client.is_connection_secure()
    mock_mail_client.is_connected.assert_called_once()


def test_is_connection_secure_gives_error(mock_mail_client):
    mock_mail_client.is_connected = MagicMock(return_value=False)
    with pytest.raises(exc.ConnectionNotEstablished):
        mock_mail_client.is_connection_secure()
    mock_mail_client.is_connected.assert_called_once()


@patch(CONTEXT_STR)
def test_secure_connection_already_secure(context_maker, mock_mail_client,
                                          mock_context):
    mock_mail_client.is_connection_secure = MagicMock(return_value=True)
    mock_mail_client.secure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    context_maker.assert_not_called()


def test_secure_connection_not_secure(mock_mail_client, mock_context,
                                      mock_client_socket, mock_ssl_socket):
    mock_mail_client.is_connection_secure = MagicMock(return_value=False)
    with patch(CONTEXT_STR, return_value=mock_context) as context_maker:
        mock_mail_client.secure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    context_maker.assert_called_once()
    mock_context.wrap_socket.assert_called_once_with(
        mock_client_socket, server_hostname='127.0.0.1')
    assert mock_mail_client._client_socket == mock_ssl_socket
    assert mock_mail_client._connection_secured


@patch(CONTEXT_STR)
def test_secure_connection_gives_error(context_maker, mock_mail_client):
    mock_mail_client.is_connection_secure = MagicMock(
        side_effect=exc.ConnectionNotEstablished('127.0.0.1', 8080))
    with pytest.raises(exc.ConnectionNotEstablished):
        mock_mail_client.secure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    context_maker.assert_not_called()


def test_create_secure_connection_not_connected(mock_mail_client):
    mock_mail_client.is_connected = MagicMock(return_value=False)
    mock_mail_client.connect = MagicMock(side_effect=None)
    mock_mail_client.secure_connection = MagicMock(side_effect=None)
    mock_mail_client.create_secure_connection()
    mock_mail_client.is_connected.assert_called_once()
    mock_mail_client.connect.assert_called_once()
    mock_mail_client.secure_connection.assert_called_once()


def test_create_secure_connection_when_connected(mock_mail_client):
    mock_mail_client.is_connected = MagicMock(return_value=True)
    mock_mail_client.connect = MagicMock()
    mock_mail_client.secure_connection = MagicMock(side_effect=None)
    mock_mail_client.create_secure_connection()
    mock_mail_client.is_connected.assert_called_once()
    mock_mail_client.connect.assert_not_called()
    mock_mail_client.secure_connection.assert_called_once()


def test_unsecure_connection_no_connection(mock_mail_client,
                                           mock_client_socket):
    mock_mail_client.is_connection_secure = MagicMock(
        side_effect=exc.ConnectionNotEstablished('127.0.0.1', 8080))
    mock_client_socket.unwrap = MagicMock()
    with pytest.raises(exc.ConnectionNotEstablished):
        mock_mail_client.unsecure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    mock_client_socket.unwrap.assert_not_called()


def test_unsecure_connection_not_secure(mock_mail_client,
                                        mock_client_socket):
    mock_mail_client.is_connection_secure = MagicMock(return_value=False)
    mock_client_socket.unwrap = MagicMock()
    with pytest.raises(exc.ConnectionNotSecure):
        mock_mail_client.unsecure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    mock_client_socket.unwrap.assert_not_called()


def test_unsecure_connection_is_secure(mock_mail_client,
                                       mock_client_socket):
    mock_mail_client.is_connection_secure = MagicMock(return_value=True)
    unsecure_socket = MagicMock()
    mock_client_socket.unwrap = MagicMock(return_value=unsecure_socket)
    mock_mail_client.unsecure_connection()
    mock_mail_client.is_connection_secure.assert_called_once()
    mock_client_socket.unwrap.assert_called_once()
    assert mock_mail_client._client_socket == unsecure_socket


def test_send_message_wait_for_reply_exception(mock_mail_client,
                                               mock_client_socket):
    mock_client_socket.send = MagicMock(side_effect=None)
    mock_mail_client.receive_and_validate_reply = MagicMock(
        side_effect=exc.UnexpectedResponseCode(530, 250))
    with pytest.raises(exc.UnexpectedResponseCode):
        mock_mail_client.send_message_wait_for_reply("HELO Matt", 1024, 250)
    mock_client_socket.send.assert_called_once_with(b'HELO Matt\r\n')
    mock_mail_client.receive_and_validate_reply.assert_called_once_with(
        1024, 250)


def test_send_message_wait_for_reply_no_exception(mock_mail_client,
                                                  mock_client_socket):
    mock_client_socket.send = MagicMock(side_effect=None)
    mock_mail_client.receive_and_validate_reply = MagicMock(side_effect=None)
    mock_mail_client.send_message_wait_for_reply("STARTTLS", 1024, 220)
    mock_client_socket.send.assert_called_once_with(b'STARTTLS\r\n')
    mock_mail_client.receive_and_validate_reply.assert_called_once_with(
        1024, 220)


def test_authenticate_no_error(mock_mail_client):
    mock_mail_client.send_message_wait_for_reply = MagicMock(side_effect=None)
    with patch(PASS_STR, return_value="Password1") as mock_pass, \
        patch(BASE64_STR, return_value=b'aX7tYltw4TG') as mock_base:
        mock_mail_client.authenticate()
    mock_pass.assert_called_once()
    mock_base.assert_called_once_with(
        b'\x00some.email@address.com\x00Password1')
    mock_mail_client.send_message_wait_for_reply.assert_called_once_with(
        "AUTH PLAIN aX7tYltw4TG", 1024, 235)


def test_authenticate_with_error(mock_mail_client):
    mock_mail_client.send_message_wait_for_reply = MagicMock(
        side_effect=exc.UnexpectedResponseCode(535, 235))
    with patch(PASS_STR, return_value="Password2") as mock_pass, \
        patch(BASE64_STR, return_value=b'x17hfdT11') as mock_base:
        with pytest.raises(exc.UnexpectedResponseCode):
            mock_mail_client.authenticate()
    mock_pass.assert_called_once()
    mock_base.assert_called_once_with(
        b'\x00some.email@address.com\x00Password2')
    mock_mail_client.send_message_wait_for_reply.assert_called_once_with(
        "AUTH PLAIN x17hfdT11", 1024, 235)


def test_initiate_secure_smtp_connection(mock_mail_client):
    mock_mail_client.connect = MagicMock(side_effect=None)
    mock_mail_client.send_message_wait_for_reply = MagicMock(side_effect=None)
    mock_mail_client.secure_connection = MagicMock(side_effect=None)
    mock_mail_client.initiate_secure_smtp_connection()
    mock_mail_client.connect.assert_called_once()
    send_calls = [call("HELO some.email@address.com", 1024, 250),
                  call("STARTTLS", 1024, 220)]
    mock_mail_client.send_message_wait_for_reply.assert_has_calls(send_calls)
    assert mock_mail_client.send_message_wait_for_reply.call_count == 2
    mock_mail_client.secure_connection.assert_called_once()
