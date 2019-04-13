from threading import Thread, Lock, Condition
import time
from random import random


class Producer(Thread):
    def run(self):
        data, capacity, lock, cv_wait, cv_notify = [
            self._kwargs[x] for x in [
                'data', 'capacity', 'lock', 'cv_wait', 'cv_notify']]
        print(data, capacity)

        while True:
            lock.acquire()
            while len(data) >= capacity:
                print("{}: queue is full".format(self.name))
                cv_wait.wait()
                print("{}: waking from space avail".format(self.name))
            data.append(None)
            print("{}: produce {}".format(self.name, data))
            cv_notify.notify()
            lock.release()
            time.sleep((random() + 0.2)/1.2)


class Consumer(Thread):
    def run(self):
        data, capacity, lock, cv_wait, cv_notify = [
            self._kwargs[x] for x in [
                'data', 'capacity', 'lock', 'cv_wait', 'cv_notify']]
        print(data, capacity)

        while True:
            lock.acquire()
            while len(data) == 0:
                print("{}: queue is empty".format(self.name))
                cv_wait.wait()
                print("{}: waking from data avail".format(self.name))
            data.pop(0)
            print("{}: consume {}".format(self.name, data))
            cv_notify.notify()
            lock.release()
            time.sleep(1.1 * (random() + 0.2)/1.2)


def main():
    q = []
    capacity = 3
    qlock = Lock()
    space_available = Condition(qlock)
    item_available = Condition(qlock)

    pargs = {
        'data': q,
        'lock': qlock,
        'capacity': capacity,
        'cv_wait': space_available,
        'cv_notify': item_available
        }
    Producer(name="p1", kwargs=pargs).start()
    Producer(name="p2", kwargs=pargs).start()
    Producer(name="p3", kwargs=pargs).start()

    cargs = {
        'data': q,
        'lock': qlock,
        'capacity': capacity,
        'cv_wait': item_available,
        'cv_notify': space_available
        }
    Consumer(name="c1", kwargs=cargs).start()
    Consumer(name="c2", kwargs=cargs).start()
    Consumer(name="c3", kwargs=cargs).start()


if __name__ == '__main__':
    main()
