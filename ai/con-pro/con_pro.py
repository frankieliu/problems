import zmq
import pickle
import os
import logging


class srvr_clnt:

    def __init__(
            self, name,
            srvr_port, clnt_port,
            call,
            input_file, output_file,
            skip_wait=False,
            begin_data=None
    ):
        self.name = name

        self.srvr_port = srvr_port
        self.clnt_port = clnt_port
        self.call = call
        self.input_file = input_file
        self.output_file = output_file
        self.cache = begin_data
        self.context = zmq.Context()
        self.message = "-"
        if skip_wait is True:
            self.task()
        else:
            self.wait_for_message()

    def wait_for_message(self):
        '''
        Waits until message is received
        '''
        logging.info("{} waiting for message".format(self.name))
        self.socket_srvr = self.context.socket(zmq.REP)
        self.socket_srvr.bind("tcp://*:{}".format(self.srvr_port))
        # self.socket_srvr.connect("tcp://localhost:{}".format(self.srvr_port))
        self.message = self.socket_srvr.recv_string()
        print("{}: received request: {}".format(self.name, self.message))
        logging.info("{} message received".format(self.name))

        # send ack back
        self.socket_srvr.send_string("ACK")

        self.task()

    def task(self):
        '''
        reads data from a file
        and perform computation on the data
        '''
        if self.cache is None:
            if os.path.exists(self.input_file):
                with open(self.input_file, "rb") as f:
                    self.cache = pickle.load(f)
            else:
                self.cache = {}

        # alternative: use system call to launch a process
        self.cache = self.call(self.cache)
        with open(self.output_file, 'wb') as f:
                pickle.dump(self.cache, f)

        print("{}: task done".format(self.name))
        self.send_message()

    def send_message(self):
        '''
        sends a message out
        '''
        self.socket_clnt = self.context.socket(zmq.REQ)
        # self.socket_clnt.bind("tcp://*:{}".format(self.clnt_port))
        self.socket_clnt.connect("tcp://localhost:{}".format(self.clnt_port))
        self.socket_clnt.send_string("{}_".format(self.message))


def srvr_clnt_launch_process(
        name,
        srvr_port, clnt_port,
        call,
        input_file, output_file,
        skip_wait=False,
        begin_data=None):

    import subclntcess

    subprocess.Popen([
        'python',
        'srvr_clnt.py',
        '-name', name,
        '-srvr_port', "{}".format(srvr_port),
        '-clnt_port', "{}".format(clnt_port),
        '-call', call,
        '-input_file', input_file,
        '-output_file', output_file,
        '-skip_wait', "{}".format(skip_wait),
        '-begin_data', "{}".format(begin_data)])


if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO)
    from local_functions import add1

    # potential functions that may be used
    tmp = add1

    parser = argparse.ArgumentParser()
    parser.add_argument('-name')
    parser.add_argument('-srvr_port')
    parser.add_argument('-clnt_port')
    parser.add_argument('-call')
    parser.add_argument('-input_file')
    parser.add_argument('-output_file')
    parser.add_argument('-skip_wait')
    parser.add_argument('-begin_data')

    args = parser.parse_args()
    print(args)
    print(args.name)
    if args.begin_data is None:
        bd = None
    else:
        bd = eval(args.begin_data)

    c = srvr_clnt(
        name=args.name,
        srvr_port=int(args.srvr_port),
        clnt_port=int(args.clnt_port),
        call=globals()[args.call],
        input_file=args.input_file,
        output_file=args.output_file,
        skip_wait=(args.skip_wait == "True"),
        begin_data=bd)
