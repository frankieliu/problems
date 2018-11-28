from heapq import heapify, heappush, heappop
import numpy as np


a = list(np.random.randint(1, 10, 10))
heapify(a)
print(a)
