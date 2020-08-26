import pytest
from Networking.Base import exceptions as exc


def test_invalid_proportion():
    with pytest.raises(exc.InvalidProportion) as prop_exc:
        raise exc.InvalidProportion(1.2)
    assert (str(prop_exc.value) == "1.2 is not a valid proportion. Please "
                                   "specify a number in the range [0, 1].")


def test_invalid_ping_count():
    with pytest.raises(exc.InvalidPingCount) as ping_exc:
        raise exc.InvalidPingCount(-1)
    assert (str(ping_exc.value) == "-1 is not a valid number of pings. "
                                   "Please specify a number greater than or "
                                   "equal to 1.")
