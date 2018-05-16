from subprocess import Popen, PIPE
# from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR

# run the shell as a subprocess:
p = Popen(['python', 'shell.py'],
          stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False,
          universal_newlines=True)

# wrap p.stdout with a NonBlockingStreamReader object:
nbsr = NBSR(p.stdout)


for i in range(0, 10):
    # issue command:
    print("Sending...")
    p.stdin.write('command\n')

    # get the output
    print("Receiving...")
    while True:
        output = nbsr.readline(0.1)
        if not output:
            print('[No more data]')
            break
        print(output)
