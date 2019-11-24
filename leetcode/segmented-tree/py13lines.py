# https://leetcode.com/problems/my-calendar-iii/discuss/214831/Python-13-Lines-Segment-Tree-with-Lazy-Propagation-O(1)-time

class MyCalendarThree(object):

    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)

    def book(self, start, end):
        def update(s, e, l = 0, r = 10**9, ID = 1):
            if r <= s or e <= l: return
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID)
                update(s, e, m, r, 2*ID+1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID], self.seg[2*ID+1])
        update(start, end)
        return self.seg[1] + self.lazy[1]

    # Time complexity O(1) - In each update, only two nodes can be
    # active at every level of the segment tree. Since the segment
    # tree has max range [0, 10**9), the depth of segment tree is
    # log(10**9) = O(1).
