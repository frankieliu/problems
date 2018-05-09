import threading
from ssh_zmq_server import ssh_zmq_server

threads = []

host = "sca-t81-135"
sp_params = {
    'user': "sunservice",
    'host': host + "-sp",
    'key': "-i /home/fyliu/.ssh/id_rsa_m8 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
    'prompt': "\[\(flash\)root@%s.+\]# " % host,
    'zmq_port': 5555}

threads.append(
    threading.Thread(target=lambda:
                     ssh_zmq_server(**sp_params)))

sys_params = {
    'user': "root",
    'host': host,
    'key': "-i /home/fyliu/.ssh/id_rsa_m8 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
    'prompt': "root@%s:.+# " % host,
    'zmq_port': 5556}

threads.append(
    threading.Thread(target=lambda:
                     ssh_zmq_server(**sys_params)))

for t in threads:
    t.start()
