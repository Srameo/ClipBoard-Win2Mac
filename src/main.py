from utils.net.core.client import ClipBoardClient
from utils.net.core.server import ClipBoardServer
import socket
import time
import threading


def serve(ip=""):
    if ip == "":
        ip = socket.gethostbyname(socket.gethostname())
    cs = ClipBoardServer(ip=ip)
    return cs


def client(ip, delay=1):
    while True:
        try:
            cc = ClipBoardClient(ip)
            return cc
        except ConnectionRefusedError:
            print("reconnect!")
            time.sleep(delay)


if __name__ == '__main__':
    threading.Thread(target=serve().run, args=()).start()
    client("10.22.140.250").run()

