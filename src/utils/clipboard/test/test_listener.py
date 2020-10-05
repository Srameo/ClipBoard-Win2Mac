from src.utils.clipboard.core.listener import Listener
import _thread

if __name__ == "__main__":
    l = Listener()
    _thread.start_new_thread(l.run(), args=())
