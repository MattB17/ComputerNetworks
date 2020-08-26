from Networking.UDPPinger import UDPClient

if __name__ == "__main__":
    client = UDPClient(1)
    client.send_ping_sequence(10, '', 12000, 1024)
