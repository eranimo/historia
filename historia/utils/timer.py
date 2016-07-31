import time


class Timer:
    def __init__(self, name, debug=True):
        self.name = name
        self.debug = debug

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        if self.debug:
            print("{} took {:0.03f} ms".format(self.name, self.interval * 1000))
