"""A collection of utility functions used in the operation of a mail client.

"""
from Networking.Base import exceptions as exc


def print_and_validate_reply(reply_msg, expected_code):
    """Prints and validates `reply_msg` based on `expected_code`.

    Parameters
    ----------
    reply_msg: str
        The message being validated. The first 3 characters of the message are
        a code, representing the server's response.
    expected_code: int
        The code expected to be found in reply message.

    Raises
    ------
    UnexpectedResponseCode
        If `reply_msg` is a message with a code other than `expected_code`.

    Returns
    -------
    None

    """
    print(reply_msg)
    actual_code = int(reply_msg[:3])
    if actual_code != expected_code:
        raise exc.UnexpectedResponseCode(actual_code, expected_code)
