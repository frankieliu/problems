import zmq
import pickle
import os


class con_pro:
    def __init__(
            self, name,
            con_port, pro_port,
            call,
            input_file, output_file):
        self.name = name
        self.con_port = con_port
        self.pro_prot = pro_port
        self.call = call
        self.input_file = input_file
        self.output_file = output_file

    def begin(self):
        self.context = zmq.Context()
        self.socket_con = self.context.socket(zmq.REP)
        self.socket_con.bind("tcp://*:{}".format(self.con_port))
        self.message = self.socket_con.recv()
        print("{}: received request: {}".format(self.name, self.message))
        self.task()

    def task(self):
        if os.path.exists(self.input_file):
            with open(self.input_file,"rb") as f:
                self.cache = pickle.load(f)
        else:
            self.cache = {}

        # alternative: use system call to launch a process
        self.cache = self.call(self.cache)
        with open(self.output_file, 'wb') as f:
                pickle.dump(self.cache, f)

        print("{}: task done".format(self.name))
        self.done()

    def done(self):
        self.socket_pro = self.context.socket(zmq.REP)
        self.socket_pro.bind("tcp://*:{}".format(self.pro_port))
        self.socket_pro.send(b"{} done.".format(self.name))
