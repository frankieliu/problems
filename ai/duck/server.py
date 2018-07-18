import zmq
import argparse


class Server:
    def __init__(self):
        self.context = zmq.Context()
        self.setupServer()

    def setupServer(self):
        self.socketServer = self.context.socket(zmq.REP)
        self.port = self.socketServer.bind_to_random_port(
            'tcp://*',
            min_port=6000,
            max_port=65000,
            max_tries=100)
        print(self.port)

    def receive(self):
        return self.socketServer.recv_string()

    def send(self, message):
        self.socketServer.send_string(message)

    def exchangePorts(self):
        while True:
            message = self.socketServer.recv_string()
            self.socketServer.send_string(message)


if __name__ == '__main__':

    Server()
