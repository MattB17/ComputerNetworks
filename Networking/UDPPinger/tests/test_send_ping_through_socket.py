import pytest
from unittest.mock import MagicMock, patch
import datetime
from Networking.UDPPinger.utils import send_ping_through_socket


FAKE_NOW = datetime.datetime(2020, 8, 22, 19, 12, 17, 701474)


@pytest.fixture(scope="function")
def datetime_now(monkeypatch):
    class DatetimeNow:
        @classmethod
        def now(cls):
            return FAKE_NOW

    monkeypatch.setattr('Networking.UDPPinger.utils.datetime', DatetimeNow)


def test_send_ping_through_socket(datetime_now):
    mock_socket = MagicMock()
    mock_socket.sendto = MagicMock(side_effect=None)
    send_ping_through_socket(3, mock_socket, "SomeHost", 1234)
    mock_socket.sendto.assert_called_once_with(
        b'ping 3 2020-08-22 19:12:17.701474', ("SomeHost", 1234))
