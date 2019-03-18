
Python fast (220ms) using heap

https://leetcode.com/problems/lfu-cache/discuss/94538

* Lang:    python3
* Author:  yorkshire
* Votes:   0

get() is O(1) since if the key already exists it updates the time and frequency, retrieves the value. It also adds the key to a set of keys to be updated later. All of these are hash map/sets.

put is O(1) if the key is already in the map. The operations here are the same as get().
put is O(log k) for a new key when the cache is not at capacity. The tuple (freq = 0, time, key) is added to heap.

It gets a bit more tricky to put() a new key when the cache is at capacity. Now we need to pop the least frequent item (ties broken by oldest) off the heap. But first we update the (freq, time) at the top of the heap if it has been updated (i.e. there has been a get or put) since the previous update. This takes O(k log k) if everything already in the cache has been get() or put() since the last new item added. 

Thanks to whoever submitted a similar idea first!

```
import heapq

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.map = {}               # key to value
        self.freq_time = {}         # key to (freq, time)
        self.priority_queue = []    # (freq, time, key), only updated when new key is added
        self.update = set()         # keys that have been get/put since last new key was added

        
    def get(self, key):
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)
            return self.map[key]
        
        return -1

    
    def put(self, key, value):
        if self.capacity <= 0:
            return 
        
        self.time += 1
        if not key in self.map:
            
            if len(self.map) >= self.capacity:      # must remove least frequent from cache
                
                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)

                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)
            
            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))
            
        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)

        self.map[key] = value
```
