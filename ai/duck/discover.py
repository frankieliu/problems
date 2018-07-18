from server import Server
from client import Client
from subprocess import Popen

num_drivers = 10
s = [None] * num_drivers
for i in range(num_drivers):
    s[i] = Server()
    print(s[i].port)

for i in range(num_drivers):
    Popen(["python", "node.py", "-pub", "{}".format(s[i].port)])

if True:
    message = ""
    for i in range(num_drivers):
        message += " " + s[i].receive()

    for i in range(num_drivers):
        s[i].send(message)
