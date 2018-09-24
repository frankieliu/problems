import pexpect
child = pexpect.spawn("ssh jitter")
child.expect("fyliu")
child.sendline("uname -a")
child.expect("fyliu")
print(child.before)
child.sendline("ls /tmp")
child.expect("fyliu")
print(child.before)
