import zmq
import argparse
import logging
from server import Server
from client import Client


class Node:
    def __init__(self, pub):
        self.pub = pub
        self.setLogger()
        self.logger.info("Creating node ns({})".format(self.pub))
        self.logger.info("Setting up server")
        self.s = Server()
        self.logger.info("Setting up ns")
        self.ns = Client(self.pub)
        self.logger.info("Exchange info with ns")
        self.exchangePorts()
        print(self.message)
        # self.setupClient()

    def setLogger(self):
        self.logger = logging.getLogger('something')
        # myFormatter = logging.Formatter(
        #    'findNodes -- %(asctime)s - %(message)s')
        myFormatter = logging.Formatter(
            'Node {}'.format(self.pub) + ' - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(myFormatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def exchangePorts(self):
        self.ns.send("{}".format(self.s.port))
        self.message = self.ns.receive()


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-pub')
    parser.add_argument('-b')
    args = parser.parse_args()
    # print(args)
    # print(args.center)
    # print("------ {}".format(args.pub))
    Node(args.pub)
