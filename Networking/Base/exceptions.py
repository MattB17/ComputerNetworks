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
