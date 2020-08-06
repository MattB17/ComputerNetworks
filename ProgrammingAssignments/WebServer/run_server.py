from WebServer import WebServer
import sys

if __name__ == "__main__":
    server = WebServer('127.0.0.1', 6789)
    server.run()
    server.close()
    sys.exit()
