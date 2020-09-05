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


def test_unexpected_response_code():
    with pytest.raises(exc.UnexpectedResponseCode) as resp_exc:
        raise exc.UnexpectedResponseCode(404, 200)
    assert (str(resp_exc.value) == "200 reply not received from the server. "
                                   "404 was returned instead.")


def test_connection_not_established():
    with pytest.raises(exc.ConnectionNotEstablished) as conn_exc:
        raise exc.ConnectionNotEstablished('smtp.gmail.com', 587)
    assert (str(conn_exc.value) == "A connection has not been established to "
                                   "smtp.gmail.com at port 587.")


def test_connection_not_secure():
    with pytest.raises(exc.ConnectionNotSecure) as conn_exc:
        raise exc.ConnectionNotSecure('smtp.gmail.com', 587)
    assert (str(conn_exc.value) == "The connection to smtp.gmail.com at port "
                                   "587 is not secure.")
