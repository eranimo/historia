import argparse
from historia.server import start_server


def main():
    parser = argparse.ArgumentParser(description='Starts a Historia server')

    parser.add_argument('-p', '--port',
        metavar='N', type=int, help='which port the server will run on', default=8888)
    parser.add_argument('-d', '--debug', action='store_true', help='Displays extra information about the simulation', default=False)

    args = parser.parse_args()

    start_server(port=args.port, debug=args.debug)
