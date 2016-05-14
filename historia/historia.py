import argparse
from historia.server import start_server


def main():
    parser = argparse.ArgumentParser(description='Starts a Historia server')
    parser.add_argument('-p', '--port',
        metavar='N', type=int, help='which port the server will run on', default=8888)
    args = parser.parse_args()

    start_server(port=args.port)
