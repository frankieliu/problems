from threading import Thread


def f(x, y, kw1=10, kw2='1'):
    print(x, y)


class fc(Thread):
    def run(self):
        print(self._kwargs)


t = Thread(target=f, kwargs={'x': 1, 'y': 2})
t.start()

fc(kwargs={'x': 1, 'y': 2}).start()
