import socket, errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(("127.0.0.1", 5555))
except socket.error as e:
    if e.errno == errno.EADDRINUSE:
        print("Port is already in use")
    else:
        # something else raised the socket.error exception
        print(e)

s.close()
