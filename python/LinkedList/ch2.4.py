# remove duplicates in linked list
import math

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
        ans = ""
        cur = self._head
        while cur != None:
            ans = ans + str(cur._value) + " "
            cur = cur._next
        print(ans)
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

    def findNfromLast(self, n):
        counter = n
        ans = None
        cur = self._head
        while cur != None:
            if counter == 0:
                ans = self._head
            elif counter < 0:
                ans = ans._next
            cur = cur._next
            counter = counter - 1
        return ans

    def remove(self, c):
        # Note cannot remove the last element!!!
        # since we can't touch

        if c is not None:
            if c._next == None:
                c = None
            else:
                c._value = c._next._value
                c._next = c._next._next
        return self

    def getN(self, n):
        counter = n;
        cur = self._head
        while cur != None:
            if counter == 0:
                return cur
            counter = counter - 1
            cur = cur._next
        return None


def addLListNumber(l1, l2):
    h1 = l1._head
    h2 = l2._head
    ans = LList()

    carry = 0
    while h1 != None and h2 != None:
        sum = h1._value + h2._value + carry
        if sum >= 10:
            ans.add(Node(sum % 10))
            carry = math.floor(sum / 10)
        else:
            ans.add(Node(sum))
            carry = 0
        h1 = h1._next
        h2 = h2._next

    if h1 == None:
        remainder = h1
    else:
        remainder = h2

    while remainder != None:
        sum = remainder._value + carry
        if sum >= 10:
            ans.add(Node(sum % 10))
            carry = math.floor(sum / 10)
        else:
            ans.add(Node(sum))
            carry = 0
        remainder = remainder._next

    if carry == 1:
        ans.add(Node(1))

    return ans


if __name__ == "__main__" :
    # store seen values in a dictionary

    # a = [2]
    a = range(0, 10)
    b = range(0, 10)
    l1 = LList()
    l2 = LList()
    [l1.add(Node(x)) for x in a]
    [l2.add(Node(x)) for x in b]
    l3 = addLListNumber(l1, l2)
    l3.print()
    print(9876543210*2)
