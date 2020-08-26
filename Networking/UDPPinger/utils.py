"""A collection of utility functions used to implement the UDP protocol for
a UDP Pinger.

"""
import random
from datetime import datetime
from Networking.Base import exceptions as exc


def validate_proportion(proportion):
    """Validates that `proportion` corresponds to a valid proportion.

    A proportion is valid if it is in the range [0, 1].

    Parameters
    ----------
    proportion: float
        The proportion to be validated.

    Raises
    ------
    InvalidProportion
        If `proportion` is not valid.

    Returns
    -------
    None

    """
    if (proportion > 1) or (proportion < 0):
        raise exc.InvalidProportion(proportion)


def create_pong(message_lst):
    """Modifies `message_lst` to create the components of a pong message.

    That is, a list is constructed representing a pong (a response) to
    `message_lst`.

    Parameters
    ----------
    message_lst: list
        A list representing the message to be replied to.

    Returns
    -------
    list
        A list with the components of a pong message which represents the
        reply to `message_lst`.

    """
    if any([word == "PING" for word in message_lst]):
        return ["PONG" if word == "PING" else word for word in message_lst]
    return ["PONG", *message_lst]


def process_message(message):
    """Processes the message given by `message`.

    `message` is a message received by a UDP node. The message is
    processed in order to derive a response message.

    Parameters
    ----------
    message: str
        A string representing a message received by a UDP node.

    Returns
    -------
    str
        A string representing the node's response to `message`.

    """
    return " ".join(create_pong(message.upper().split()))


def will_drop_message(reliability):
    """Determines if a message will be dropped by a UDP node.

    A message is deemed dropped if it is either not successfully
    received or is not successfully sent.

    Parameters
    ----------
    reliability: float
        A float representing the reliability of a UDP node. This is a
        number between 0 and 1 representing the long run proportion
        of messages dropped by the node.

    Returns
    -------
    bool
        True if the message will be dropped. Otherwise, False.

    """
    r = random.randint(1, 100)
    return r <= (1 - reliability) * 100


def get_rtt_from_pong_message(pong_message, received_time):
    """Calculates the round trip time based on `pong_message`.

    `pong_message` is a space separated string consisting of 3 components.
    The first identifies the message as a pong message (a ping response).
    The second is the message count, and the third is the time at which
    the ping message was sent. This third component is used to calculate
    the round trip time.

    Parameters
    ----------
    pong_message: str
        A string representing a pong message.
    received_time: datetime.datetime
        A datetime representing the point in time at which `pong_message`
        was received.

    Returns
    -------
    int
        An integer representing the round trip time (the time between when
        the original ping was sent and when the pong was received) in
        milliseconds.

    """
    sent_time_str = " ".join(pong_message.split()[2:])
    sent_time = datetime.strptime(sent_time_str, "%Y-%m-%d %H:%M:%S.%f")
    return int((received_time - sent_time).total_seconds() * 1000000)


def validate_ping_count(ping_count):
    """Validates that `ping_count` represents a valid number of pings to send.

    Parameters
    ----------
    ping_count: int
        An integer representing the number of ping messages to be sent.

    Raises
    ------
    InvalidPingCount
        If `ping_count` does not represent a valid number of pings to send.
        That is, if `ping_count` is less than or equal to 0.

    Returns
    -------
    None

    """
    if ping_count <= 0:
        raise exc.InvalidPingCount(ping_count)
