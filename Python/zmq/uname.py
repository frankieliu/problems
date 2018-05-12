import subprocess
import sys

HOST = "jitter"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND = "uname -a"

ssh = subprocess.Popen(
    ["ssh", "-i", "/home/fyliu/.ssh/id_rsa", "%s" % HOST, COMMAND],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print(result)
