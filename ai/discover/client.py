import zmq
import argparse


class Client:
    def __init__(self, pub):
        self.pub = pub
        self.context = zmq.Context()
        self.setupClient()
        # self.exchangePorts()

    def setupClient(self):
        '''
        nameserver client
        '''
        self.socketClient = self.context.socket(zmq.REQ)
        self.socketClient.connect("tcp://localhost:{}".format(self.pub))

    def send(self, message):
        self.socketClient.send_string(message)

    def receive(self):
        self.message = self.socketClient.recv_string()
        return self.message

    def exchangePorts(self):
        while True:
            a = input("> ")
            self.socketClient.send_string("{}".format(a))
            self.message = self.socketClient.recv_string()
            print("Received: " + self.message)


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-pub')
    parser.add_argument('-b')
    args = parser.parse_args()
    # print(args)
    # print(args.center)
    # print("------ {}".format(args.pub))
    Client(args.pub)
