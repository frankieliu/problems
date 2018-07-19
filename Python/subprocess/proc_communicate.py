import subprocess


proc = subprocess.Popen(
    ['cdrecord', '--help'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
print('stdout:', out)
print('stderr:', err)
