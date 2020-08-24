import pytest
import datetime
import sys
import io
from unittest.mock import MagicMock, patch
from Networking.UDPPinger.udp_client import UDPClient
from socket import AF_INET, SOCK_DGRAM, timeout


SOCKET_STR = "socket.socket"
FAKE_NOW = datetime.datetime(2020, 8, 22, 19, 12, 17, 701474)
RTT_STR = "Networking.UDPPinger.utils.get_rtt_from_pong_message"


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


@pytest.fixture(scope="function")
def datetime_now(monkeypatch):
    class DatetimeNow:
        @classmethod
        def now(cls):
            return FAKE_NOW
    monkeypatch.setattr(
        'Networking.UDPPinger.udp_client.datetime', DatetimeNow)


@pytest.fixture(scope="function")
def mock_addr():
    return MagicMock()


def test_instantiation(mock_udp_client, mock_client_socket):
    assert mock_udp_client.get_socket_timeout() == 3
    mock_client_socket.gettimeout.assert_called_once()


def test_send_ping(mock_udp_client, mock_client_socket, datetime_now):
    mock_client_socket.sendto = MagicMock(side_effect=None)
    mock_udp_client.send_ping(3, "SomeHost", 1234)
    mock_client_socket.sendto.assert_called_once_with(
        b'ping 3 2020-08-22 19:12:17.701474', ("SomeHost", 1234))


def test_receive_and_decode_empty_message(mock_udp_client, mock_addr,
                                          mock_client_socket):
    mock_client_socket.recvfrom = MagicMock(return_value=(b'', mock_addr))
    assert mock_udp_client.receive_and_decode_message(1024) == ""
    mock_client_socket.recvfrom.assert_called_once_with(1024)


def test_receive_and_decode_non_empty_message(mock_udp_client, mock_addr,
                                              mock_client_socket):
    mock_client_socket.recvfrom = MagicMock(
        return_value=(b'PONG 5 2020-08-22 19:20:35.175', mock_addr))
    assert (mock_udp_client.receive_and_decode_message(2048) ==
            "PONG 5 2020-08-22 19:20:35.175")
    mock_client_socket.recvfrom.assert_called_once_with(2048)


def test_receive_and_decode_message_with_error(mock_udp_client,
                                               mock_client_socket):
    mock_client_socket.recvfrom = MagicMock(side_effect=timeout)
    with pytest.raises(timeout):
        mock_udp_client.receive_and_decode_message(3072)
    mock_client_socket.recvfrom.assert_called_once_with(3072)


def test_send_ping_wait_for_response_exception(mock_udp_client):
    mock_udp_client.send_ping = MagicMock(side_effect=None)
    mock_udp_client.receive_and_decode_message = MagicMock(
        side_effect=timeout)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    with patch(RTT_STR) as mock_rtt:
        mock_udp_client.send_ping_wait_for_response(3, "SomeHost", 1234, 1024)
    sys.stdout = sys.__stdout__
    mock_udp_client.send_ping.assert_called_once_with(3, "SomeHost", 1234)
    mock_udp_client.receive_and_decode_message.assert_called_once_with(1024)
    mock_rtt.assert_not_called()
    assert str(captured_output.getvalue()) == "Request timed out\n"


def test_send_ping_wait_for_response_no_exception(mock_udp_client,
                                                  datetime_now):
    received_message = "PONG 5 2020-08-22 19:12:16.201474"
    mock_udp_client.send_ping = MagicMock(side_effect=None)
    mock_udp_client.receive_and_decode_message = MagicMock(
        return_value=received_message)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    with patch(RTT_STR, return_value=2500) as mock_rtt:
        mock_udp_client.send_ping_wait_for_response(5, "AHost", 5678, 2048)
    sys.stdout = sys.__stdout__
    mock_udp_client.send_ping.assert_called_once_with(5, "AHost", 5678)
    mock_udp_client.receive_and_decode_message.assert_called_once_with(2048)
    mock_rtt.assert_called_once_with(received_message, FAKE_NOW)
    assert str(captured_output.getvalue()) == "{}\nRTT of 2500 ms\n".format(
        received_message)
