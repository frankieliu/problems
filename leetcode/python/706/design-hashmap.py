"""706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the
value already exists in the HashMap, update the value.

get(key): Returns the value to which the specified key is mapped, or
-1 if this map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map
contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 10000
        # each bucket has a key and a value
        # [keys:, values:]
        self.b = [[[], []] for i in range(0, self.n)]

    def hash(self, key):
        return key % self.n

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        b, i = self.find_bucket(key)
        if i == -1:
            b[0].append(key)
            b[1].append(value)
        else:
            b[1][i] = value

    def find_bucket(self, key):
        bidx = self.hash(key)    # bucket index
        bucket = self.b[bidx]
        keys = bucket[0]
        print("Finding bucket", key, bidx, bucket, keys)
        for i in range(0, len(keys)):
            if key == keys[i]:
                return bucket, i
        return bucket, -1

    def get(self, key):
        """Returns the value to which the specified key is mapped, or -1 if
        this map contains no mapping for the key

        :type key: int
        :rtype: int
        """
        b, i = self.find_bucket(key)
        print("get", b, i)
        if i == -1:
            return -1
        return b[1][i]

    def remove(self, key):
        """Removes the mapping of the specified value key if this map contains
        a mapping for the key

        :type key: int
        :rtype: void

        """
        b, i = self.find_bucket(key)
        if i == -1:
            return
        print("Removing", key, b, i)
        b[0].pop(i)
        b[1].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))  # returns 1
print(hashMap.get(3))  # returns -1 (not found)
hashMap.put(2, 1)      # update the existing value
print(hashMap.get(2))  # returns 1
hashMap.remove(2)      # remove the mapping for 2
print(hashMap.get(2))  # returns -1 (not found)
