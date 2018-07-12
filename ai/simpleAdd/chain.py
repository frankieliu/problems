import logging
from srvr_clnt import srvr_clnt_launch_process as launch

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    port = 5560

    # seeding the chain
    launch("c{}".format(port),
           0, port + 1,
           "add1",
           "",
           "c{}_out".format(port),
           no_server=True,
           begin_data=10)

    port += 1

    launch("c{}".format(port),
           port, port + 1,
           "add1",
           "c{}_out".format(port - 1),
           "c{}_out".format(port))

    port += 1

    launch("c{}".format(port),
           port, port + 1,
           "add1",
           "c{}_out".format(port - 1),
           "c{}_out".format(port))

    port += 1

    # terminating the chain
    launch("c{}".format(port),
           port, 0,
           "add1",
           "c{}_out".format(port - 1),
           "c{}_out".format(port),
           no_client=True)
