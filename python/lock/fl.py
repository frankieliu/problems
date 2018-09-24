from flufl.lock import Lock
import multiprocessing
import time
from datetime import timedelta

def attempt_lock(filename, lifetime, queue):
    t0 = time.time()
    # if you acquire a look inform parent
    with Lock(filename, lifetime):
        queue.put(time.time() - t0)
        # keep the lock for lifetime
        time.sleep(lifetime.seconds - 1)

def acquire(filename, lifetime=None):
    queue = multiprocessing.Queue()
    # fork a process to acquire a lock pass a message queue
    proc = multiprocessing.Process(
        target=attempt_lock,
        args=(filename, lifetime, queue))
    proc.start()

    # wait until lock is acquired
    acq_time = queue.get()
    print("It took ", acq_time, " to get a lock")


if __name__ == "__main__":

    import sys
    import os

    filename = "test1.lck"
    locktime = timedelta(seconds=10)

    try:
        print(os.getpid(), ": Acquiring lock")
        acquire(filename, locktime)
        # the lock has been acquired, do some useful stuff
        # ...

        # attempt to get another lock:
        lock = Lock(filename, locktime)

        # will hang at the next line until the lock is released
        print(os.getpid(), ": Acquiring second lock")
        lock.lock()
        print(os.getpid(), lock.is_locked)

    except:
        print(sys.exc_info()[0])
