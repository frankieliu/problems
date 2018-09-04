# remove duplicates in linked list

class Node:
    def __init__(self, value):
        self._next = None
        self._value = value

class LList:
    def __init__(self):
        self._head = None
        self._last = self._head

    def add(self,n):
        if self._head == None:
            self._head = n
            self._last = n
        else:
            self._last._next = n
            self._last = n
        return self

    def print(self):
        cur = self._head
        while cur != None:
            print(cur._value)
            cur = cur._next
        return self

    def dedup(self):
        h = {}
        cur = self._head
        while cur != None:
            if cur._value in h:
                # skip it (need previous pointer)
                prev._next = cur._next
            else:
                h[cur._value] = True
                prev = cur
            cur = prev._next
        return self

    def inL(self, value, lastN):
        if lastN is None:
            return False
        cur = self._head
        while cur != None and cur != lastN._next:
            if cur._value == value:
                return True
            cur = cur._next
        return False

    def dedupNoDict(self):
        cur = self._head
        prev = None
        while cur != None:
            if self.inL(cur._value, prev):
                prev._next = cur._next
            else:
                prev = cur
            cur = prev._next
        return self


if __name__ == "__main__" :
    # store seen values in a dictionary
    l = LList()
    # a = [2]
    a = [2, 3, 4, 3, 3, 4, 4, 5, 2, 2, 3, 5]
    [l.add(Node(x)) for x in a]
    # l.dedup().print()
    l.dedupNoDict().print()
