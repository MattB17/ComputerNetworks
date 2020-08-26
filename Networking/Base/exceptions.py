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
