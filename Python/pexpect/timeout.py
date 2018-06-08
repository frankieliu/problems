import pexpect
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--port', help="port (host) number to connect to",
                    default=133)
args = parser.parse_args()
port = args.port

try:
    child = pexpect.spawn("ssh -o ConnectTimeout=5 sca-t81-{}".format(port),
                          timeout=2)
except pexpect.exceptions.EOF:
    print("doesn't catch anything here")
    sys.exit()
except Exception as e:
    print("general exception", e)
    sys.exit()

while True:
    try:
        '''
        \x1b[0;32msca-t81-133\x1b[m
        \x1b[1;34m~\x1b[m \x1b[1;32m$ \x1b[m\x1b[0m ~
        '''
        index = child.expect(
            r'\x1B\[0;32msca.+\x1B\[1;32m\$ \x1B\[m\x1B\[0m ',
            timeout=1)
        print("BEFORE: ", child.before.decode("utf-8"))
        print("AFTER: ", child.after.decode("utf-8"))
        cmd = input("Enter: ")
        child.sendline(cmd)
    except pexpect.TIMEOUT:
        # print(child.before)
        # print(child.after)
        # print(child.after == pexpect.TIMEOUT)
        print("Timeout")
    except pexpect.exceptions.EOF:
        print("Cannot connect")
        print("Rebooting the machine")
        break
    except:
        raise
