import pytest
from unittest.mock import MagicMock
from Networking.UDPPinger.utils import receive_and_decode_message


@pytest.fixture(scope="function")
def mock_addr():
    return MagicMock()


@pytest.fixture(scope="function")
def mock_socket():
    return MagicMock()


def test_empty_message(mock_socket, mock_addr):
    mock_socket.recvfrom = MagicMock(return_value=(b'', mock_addr))
    assert receive_and_decode_message(mock_socket, 1024) == ""
    mock_socket.recvfrom.assert_called_once_with(1024)


def test_non_empty_message(mock_socket, mock_addr):
    mock_socket.recvfrom = MagicMock(
        return_value=(b'PONG 5 2020-08-22 19:20:35.175', mock_addr))
    assert (receive_and_decode_message(mock_socket, 2048) ==
            "PONG 5 2020-08-22 19:20:35.175")
    mock_socket.recvfrom.assert_called_once_with(2048)
