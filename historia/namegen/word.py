import random
import os

def random_word():
    filename = os.path.dirname(__file__)
    return random.choice(open(filename + '/names.txt').read().splitlines())


if __name__ == '__main__':
    for i in range(50):
        print(random_word())
