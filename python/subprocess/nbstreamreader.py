from threading import Thread
from queue import Queue, Empty


class UnexpectedEndOfStream(Exception):
    pass


class NonBlockingStreamReader:
    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usuallly a process' stdout or stderr
        '''
        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            '''
            Collect lines from 'stream' and put them in 'queue'
            '''
            print(stream)
            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                    print("Adding to queue {}\n".format(line))
                else:
                    raise UnexpectedEndOfStream

        self._t = Thread(target=_populateQueue,
                         args=(self._s, self._q))
        self._t.daemon = True
        print("Starting queue\n")
        self._t.start()  # start collecting lines from the stream

    def readline(self, timeout=None):
        try:
            return self._q.get(block=timeout is not None,
                               timeout=timeout)
        except Empty:
            return None
