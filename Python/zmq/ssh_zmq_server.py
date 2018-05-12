# Binds REP socket to tcp://*:5555

import zmq
import pexpect


class ssh_zmq_server():

    def __init__(self,
                 user="sunservice",
                 host="ca-t81-133",
                 key="-i /home/fyliu/.ssh/id_rsa_m8",
                 prompt="\[\(flash\)root@sca-t.+\]# ",
                 zmq_port="5555"):

        # start ssh session
        self.user = user
        self.host = host
        self.key = key
        self.prompt = prompt
        self.child = pexpect.spawn(
            "ssh %s %s" % (self.key, self.user + "@" + self.host))
        self.child.expect(self.prompt)
        self.child.setecho(False)

        # open a zmq context
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % zmq_port)

        # begin loop
        self.loop()

    def loop(self):
        # main loop
        while True:
            #  Wait for next request from client
            message = self.socket.recv_string()
            print("Received request: %s" % message)

            self.child.sendline(message)
            self.child.expect(self.prompt)
            out = self.child.before

            # Send message back to client
            self.socket.send(out)
            print("Sending reponse: %s " % out.decode())
