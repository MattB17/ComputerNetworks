"""A collection of utility functions used to implement the UDP protocol for
a UDP Pinger.

"""
import random


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
