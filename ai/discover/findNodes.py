import logging
import zmq
from subprocess import Popen, PIPE


'''
1. create bindings to drivers' comm ports
2. launch the drivers with given ports
3. expect req from drivers
4. send back connections to drivers
5. turn center off
'''

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger('something')
    # myFormatter = logging.Formatter('findNodes -- %(asctime)s - %(message)s')
    myFormatter = logging.Formatter('findNodes - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(myFormatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    context = zmq.Context()

    # open a bunch of server sockets
    logger.info("opening server sockets")
    num_drivers = 2
    sockets = [context.socket(zmq.REP)] * num_drivers
    ports = [sockets[i].bind_to_random_port(
        'tcp://*',
        min_port=6000,
        max_port=65000,
        max_tries=100) for i in range(num_drivers)]

    for i in range(num_drivers):
        logger.info("Ports {}: {}".format(i, ports[i]))

    '''
    # begin node processes
    logger.info("beginning node processes")
    procs = [None] * num_drivers
    for i in range(num_drivers):
        procs[i] = Popen(
            ['python', 'node.py', '-pub', "{}".format(ports[i])])
    '''

    # receive ports from nodes
    logger.info("receive data from nodes")
    message = ""
    for i in range(num_drivers):
        message += "{}".format(sockets[i].recv())

    # reply back with "messages"
    logger.info("reply back with messages")
    for i in range(num_drivers):
        sockets[i].send_string(message)
