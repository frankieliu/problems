# http://kitchingroup.cheme.cmu.edu/blog/2013/06/20/Memoizing-expensive-functions-in-python-and-saving-results/
import os
import pickle
from functools import wraps


def memoize(func):
    if os.path.exists('memoize.pkl'):
        print('reading cache file')
        with open('memoize.pkl') as f:
            cache = pickle.load(f)
    else:
        cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            print('Running func')
            cache[args] = func(*args)
            # update the cache file
            with open('memoize.pkl', 'wb') as f:
                pickle.dump(cache, f)
        else:
            print('result in cache')
        return cache[args]
    return wrap


@memoize
def myfunc(a):
    return a**2


print(myfunc(2))
print(myfunc(2))

print(myfunc(3))
print(myfunc(2))
