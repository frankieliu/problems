import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
port_selected = socket.bind_to_random_port(
    'tcp://*', min_port=6001,
    max_port=10000, max_tries=100)
