#   Binds REP socket to tcp://*:5555
#
# import time

import zmq
import subprocess

host = "jitter"
ssh = subprocess.Popen(["ssh", "-i", "/home/fyliu/.ssh/id_rsa", "%s" % host],
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       universal_newlines=True,
                       bufsize=0)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    #  Wait for next request from client
    message = socket.recv_string()
    print("Received request: %s" % message)

    ssh.stdin.write(message + "\n")
    out = ssh.stdout.readline()

    # out, err = ssh.communicate(message)

    # Send reply back to client
    # socket.send_string("World")
    # socket.send_string(line)
    # socket.send_string("__END__")

    socket.send_string(out)
