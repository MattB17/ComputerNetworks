"""A collection of custom exceptions generated when dealing with the
networking applications.

"""


class InvalidProportion(Exception):
    """An Exception when `prop` does not correspond to a valid proportion.

    Parameters
    ----------
    prop: float
        The number that generated the exception.

    """
    def __init__(self, prop):
        message = ("{} is not a valid proportion. Please specify a number in "
                   "the range [0, 1].".format(prop))
        Exception.__init__(self, message)


class InvalidPingCount(Exception):
    """An Exception when `ping_count` is less than or equal to 0.

    The Exception is generated when a class or method tries to send a
    sequence of pings but the number of pings specified to be sent is
    less than or equal to 0.

    Parameters
    ----------
    ping_count: int
        The number of pings to be sent.

    """
    def __init__(self, ping_count):
        message = ("{} is not a valid number of pings. Please specify a "
                   "number greater than or equal to 1.".format(ping_count))
        Exception.__init__(self, message)


class UnexpectedResponseCode(Exception):
    """An Exception when `actual_code` and `expected_code` do not match.

    The Exception is generated when a client expects `expected_code` to be
    returned by the server but `actual_code` was returned instead.

    Parameters
    ----------
    actual_code: int
        An integer representing the actual code returned by the server.
    expected_code: int
        An integer representing the code expected to be returned by the
        server.

    """
    def __init__(self, actual_code, expected_code):
        message = ("{0} reply not received from the server. {1} was "
                   "returned instead.".format(expected_code, actual_code))
        Exception.__init__(self, message)


class ConnectionNotEstablished(Exception):
    """An Exception when a connection has not been established.

    This Exception is generated for connection based protocols, such as TCP,
    when a user tries to access a connection that has not yet been
    established.

    Parameters
    ----------
    host: str
        The name of the host for which the connection should be established.
    port: int
        The port number at the host which will accept the connection.

    """
    def __init__(self, host, port):
        message = ("A connection has not been established to {0} at "
                   "port {1}.".format(host, port))
        Exception.__init__(self, message)


class ConnectionNotSecure(Exception):
    """An Exception when a connection has not been secured.

    This Exception is generated when a user accesses a connection assuming
    it is secure but, in fact, the connection has not been secured.

    Parameters
    ----------
    host: str
        The name of the host for which the connection is unsecure.
    port: int
        The port number to which the unsecure connection points.

    """
    def __init__(self, host, port):
        message = "The connection to {0} at port {1} is not secure.".format(
            host, port)
        Exception.__init__(self, message)
