import pytest
from unittest.mock import MagicMock, patch
from Networking.WebServer.utils import render_page


READ_STR = "Networking.WebServer.utils.read_message"
SEND_STR = "Networking.WebServer.utils.send_data_through_socket"


@pytest.fixture(scope="function")
def mock_socket():
    socket = MagicMock()
    socket.send = MagicMock(side_effect=None)
    socket.close = MagicMock(side_effect=None)
    return socket


@patch(SEND_STR, side_effect=None)
def test_without_error(mock_send, mock_socket):
    mock_socket.recv = MagicMock(
        return_value=b'http://some/url /some_page.html')
    data = ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n']
    with patch(READ_STR, return_value=data) as mock_read:
        render_page(mock_socket)
    mock_socket.recv.assert_called_once_with(1024)
    mock_read.assert_called_once_with('http://some/url /some_page.html')
    mock_send.assert_called_once_with(mock_socket, data)
    mock_socket.close.assert_called_once()


@patch(SEND_STR)
@patch(READ_STR)
def test_with_error(mock_read, mock_send, mock_socket):
    mock_socket.recv = MagicMock(side_effect=IOError)
    render_page(mock_socket)
    mock_socket.recv.assert_called_once_with(1024)
    mock_read.assert_not_called()
    mock_send.assert_not_called()
    mock_socket.send.assert_called_once_with(
        b'HTTP/1.1 404 Not Found\r\n\r\n')
    mock_socket.close.assert_called_once()
