import pyperclip
import time


class Listener:

    old_string = ""
    delay = 0.5
    func = print

    def __init__(self, delay=0.5, func=print):
        self.old_string = pyperclip.paste()
        self.delay = delay
        self.func = func

    def run(self):
        while True:
            time.sleep(self.delay)
            string = pyperclip.paste()
            if string != self.old_string and string != "":
                self.func(string)
                print("new string is:\n" + string)
                if string == "sr@meo":
                    print("quit clipboard listener!")
                    break
                self.old_string = string
