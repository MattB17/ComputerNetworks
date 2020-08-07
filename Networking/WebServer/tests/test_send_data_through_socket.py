import pytest
from unittest.mock import MagicMock, call
from Networking.WebServer.utils import send_data_through_socket


OK_MESSAGE = "HTTP/1.1 200 OK\r\n\r\n".encode()
END_MESSAGE = "\r\n".encode()


@pytest.fixture(scope="function")
def mock_socket():
    socket = MagicMock()
    socket.send = MagicMock(side_effect=None)
    return socket


def test_with_empty_list(mock_socket):
    send_data_through_socket(mock_socket, [])
    socket_calls = [call(OK_MESSAGE), call(END_MESSAGE)]
    mock_socket.send.assert_has_calls(socket_calls)
    assert mock_socket.send.call_count == 2


def test_with_one_element_list(mock_socket):
    data = ['data\n']
    encoded_data = ['data\n'.encode()]
    send_data_through_socket(mock_socket, data)
    socket_calls = [
        call(OK_MESSAGE), call(encoded_data[0]), call(END_MESSAGE)]
    mock_socket.send.assert_has_calls(socket_calls)
    assert mock_socket.send.call_count == 3


def test_with_multi_element_list(mock_socket):
    data = ['line1\n', 'line2\n', 'line3\n']
    encoded_data = [
        'line1\n'.encode(), 'line2\n'.encode(), 'line3\n'.encode()]
    send_data_through_socket(mock_socket, data)
    socket_calls = ([call(OK_MESSAGE)] +
                    [call(encoded) for encoded in encoded_data] +
                    [call(END_MESSAGE)])
    mock_socket.send.assert_has_calls(socket_calls)
    assert mock_socket.send.call_count == 5
