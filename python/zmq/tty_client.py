#   Binds REP socket to tcp://*:5555

import zmq
import argparse

# Get port number
parser = argparse.ArgumentParser()
parser.add_argument('-p')
args = parser.parse_args()
port = args.p

#  Socket to server
print("Connecting to …")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

while True:
    request = input("Enter: ")
    if request in ['q', 'Q']:
        break
    else:
        # Sending request
        print("Sending request: %s" % request)
        socket.send_string(request)

        # Get the reply.
        message = socket.recv_string()
        print("Received reply: %s" % message)
