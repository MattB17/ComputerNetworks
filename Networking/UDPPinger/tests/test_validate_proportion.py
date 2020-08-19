import pytest
from Networking.Base import exceptions as exc
from Networking.UDPPinger.utils import validate_proportion


def test_proportion_too_low():
    with pytest.raises(exc.InvalidProportion):
        validate_proportion(-0.5)


def test_proportion_too_high():
    with pytest.raises(exc.InvalidProportion):
        validate_proportion(1.2)


def test_zero_proportion():
    validate_proportion(0)


def test_one_proportion():
    validate_proportion(1)


def test_middle_proportion():
    validate_proportion(0.7)
