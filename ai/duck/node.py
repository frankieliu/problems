import zmq
import argparse
from setLogger import setLogger
from server import Server
from client import Client


class Node:
    def __init__(self, pub):

        self.pub = pub

        self.logPrefix = "Node {}".format(self.pub)
        setLogger(self)

        self.info("Creating node sequencer({})".format(self.pub))
        self.info("Setting up sequencer server")
        self.s = Server()

        self.info("Setting up sequencer client to discovery unit")
        self.ns = Client(self.pub)

        self.info("Exchange info with discovery unit")
        self.exchangePorts()
        print(self.message)
        # self.setupClient()

    def exchangePorts(self):
        self.ns.send("{}".format(self.s.port))
        self.message = self.ns.receive()


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-pub')
    parser.add_argument('-clambda')
    args = parser.parse_args()

    # Sequencing unit
    n = Node(args.pub)
    if args.lmb is not None:
        # Get the class
        clambda = getattr(__import__(args.clambda), args.clambda)
        cl = clambda(n)
        print(cl.desc())
