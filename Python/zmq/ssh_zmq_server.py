#   Binds REP socket to tcp://*:5555
#
# import time

import zmq
import pexpect

# start ssh session
host = "sunservice@sca-t81-133-sp"
key = "-i /home/fyliu/.ssh/id_rsa_m8"
child = pexpect.spawn("ssh %s %s" % (key, host))
prompt = "\[\(flash\)root@sca-t.+\]# "

# open a zmq context
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# main loop
while True:

    #  Wait for next request from client
    message = socket.recv_string()

    print("Received request: %s" % message)
    child.sendline(message)
    child.expect(prompt)
    out = child.before

    # Send message back to client
    socket.send(out)
