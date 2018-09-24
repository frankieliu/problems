import pexpect


child = pexpect.spawn("bash")
index = child.expect(r'\$ \x1B\[m\x1B\[0m ')
print("BEFORE: ", child.before)
print("MATCH: ", child.match)
print("AFTER: ", child.after)
child.interact()
