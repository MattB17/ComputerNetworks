from Networking.UDPPinger import UDPServer

if __name__ == "__main__":
    server = UDPServer('', 12000, 0.7)
    server.run()
