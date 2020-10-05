from src.utils.net.core.client import ClipBoardClient
from src.utils.net.core.server import ClipBoardServer

if __name__ == '__main__':
    cc = ClipBoardClient("10.22.180.13")
    cs = ClipBoardServer()
    cc.run()
    cs.run()
