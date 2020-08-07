
def read_message(message):
    filename = message.split()[1]
    with open(filename[1:], "r") as f:
        output_data = f.readlines()
    return output_data
