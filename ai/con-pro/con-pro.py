import time
import zmq


class con_pro:

context = zmq.Context()
socket_in = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

message = socket.recv()
print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
