import time


class Timer:
    def __init__(self, text, debug=True):
        self.text = text
        self.debug = debug

    def __enter__(self):
        if self.debug:
            print(self.text.ljust(50), end="")
            print('starting...')
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        if self.debug:
            print(self.text.ljust(50), end="")
            print("finished after {:0.03f} ms\n".format(self.interval * 1000))
