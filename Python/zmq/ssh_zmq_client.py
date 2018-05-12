#   Binds REP socket to tcp://*:5555

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send_string("ls /tmp")

    # Get the reply.
    message = socket.recv_string()
    print("Received reply %s [ %s ]" % (request, message))

    # while (message != "__END__"):
    # message = socket.recv_string()
    # print("Received reply %s [ %s ]" % (request, message))
