import pytest
from Networking.Base import exceptions as exc
from Networking.UDPPinger.utils import validate_ping_count


def test_negative_int():
    with pytest.raises(exc.InvalidPingCount):
        validate_ping_count(-3)


def test_zero():
    with pytest.raises(exc.InvalidPingCount):
        validate_ping_count(0)


def test_positive_int():
    validate_ping_count(2)
