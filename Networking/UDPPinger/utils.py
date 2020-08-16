"""A collection of utility functions used to implement the UDP protocol for
a UDP Pinger.

"""


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
