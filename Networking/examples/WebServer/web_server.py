from Networking.WebServer import WebServer
import sys

if __name__ == "__main__":
    server = WebServer('', 6789)
    server.run()
    server.close()
    sys.exit()
