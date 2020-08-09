
def read_message(message):
    filename = message.split()[1]
    with open(filename[1:], "r") as f:
        return f.readlines()


def send_data_through_socket(socket, data):
    socket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    for i in range(0, len(data)):
        socket.send(data[i].encode())
    socket.send("\r\n".encode())


def render_page(socket):
    try:
        message = socket.recv(1024).decode()
        output_data = read_message(message)
        send_data_through_socket(socket, output_data)
    except IOError:
        socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    finally:
        socket.close()
