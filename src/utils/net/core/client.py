import socket
import threading
from utils.clipboard.core.listener import Listener


class ClipBoardClient:
    s = None
    clients = 1

    def __init__(self, ip, port=37657):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 服务器之间的数据流,tcp通信
        self.s.connect((ip, port))
        print(self.s.recv(1024).decode("utf-8"))

    def send(self, string):
        self.s.send(string.encode("utf-8"))

    def run(self):
        ls = Listener(func=self.send)
        t = threading.Thread(target=ls.run, args=())
        t.start()
