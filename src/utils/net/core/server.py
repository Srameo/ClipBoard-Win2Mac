import socket
import threading
import time
import pyperclip


def service(sock, addr):
    print("接收到来自%s:%s连接请求" % addr)  # addr包括IP和Port
    sock.send(b"connected!")
    while True:
        message = sock.recv(1024)  # 1024??
        time.sleep(0.5)  # 延时0.5秒，没接收到数据或者exit则退出
        if not message or message.decode("utf-8") == "sr@meo":
            break
        pyperclip.copy(message.decode("utf-8"))
    sock.close()
    print("已关闭TCP")


class ClipBoardServer:

    s = None
    clients = 1

    def __init__(self, ip="127.0.0.1", port=37657, clients=1):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 服务器之间的数据流,tcp通信
        self.s.bind((ip, port))
        self.s.listen(clients)  # 最大连接数量，监听
        self.clients = clients
        print("等待连接.....")

    def run(self):
        count = 0
        while count < self.clients:
            sock, addr = self.s.accept()  # 获取新连接的地址端口
            count += 1
            t = threading.Thread(target=service, args=(sock, addr))  # 线程运行函数,参数
            t.start()  # 开启线程
