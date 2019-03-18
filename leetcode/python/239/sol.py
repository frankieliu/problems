
9 lines Ruby, 11 lines Python, O(n)

https://leetcode.com/problems/sliding-window-maximum/discuss/65901

* Lang:    python3
* Author:  StefanPochmann
* Votes:   50

Keep indexes of good candidates in deque `d`. The indexes in `d` are from the current window, they're increasing, and their corresponding `nums` are decreasing. Then the first deque element is the index of the largest window value.

For each index `i`:

1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index `i - k`, if it's still in the deque (it falls out of the window).
4. If our window has reached size `k`, append the current window maximum to the output.

---

**Ruby**

Apparently Ruby doesn't have a deque, so I simulate one with an array, where `s` tells the start index of the queue in the array.

    def max_sliding_window(nums, k)
        d, s = [], 0
        out = []
        nums.each_index{ |i|
            d.pop while d[s] && nums[d[-1]] < nums[i]
            d << i
            s += 1 if d[s] == i - k
            out << nums[d[s]] if i >= k - 1
        }
        out
    end

---

**Python**

    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

Last three lines could be this, but for relatively large k it would waste space:

            out += nums[d[0]],
        return out[k-1:]
