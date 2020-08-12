"""A collection of utility functions used to help render a web server.

"""


def read_message(message):
    """Reads `message`.

    Parameters
    ----------
    message: str
        A string specifying the message to be read. This is a space delimited
        string where the second word specifies the name of the file to be
        read.

    Returns
    -------
    list
        A list of strings representing the lines of the file specified by
        `message`.

    """
    filename = message.split()[1]
    with open(filename[1:], "r") as f:
        return f.readlines()


def send_data_through_socket(socket, data):
    """Sends `data` through `socket`.

    Parameters
    ----------
    socket: socket.socket
        The socket through which `data` is sent.
    data: list
        A list of strings specifying the data to be sent through `socket`.

    Returns
    -------
    None

    """
    socket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    for i in range(0, len(data)):
        socket.send(data[i].encode())
    socket.send("\r\n".encode())


def render_page(socket):
    """Uses `socket` to render the requested page.

    If the requested page exists then it is rendered. Otherwise, a 404 error
    is generated.

    Parameters
    ----------
    socket: socket.socket
        The socket used to render the page.

    Returns
    -------
    None

    """
    try:
        message = socket.recv(1024).decode()
        output_data = read_message(message)
        send_data_through_socket(socket, output_data)
    except IOError:
        socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    finally:
        socket.close()
