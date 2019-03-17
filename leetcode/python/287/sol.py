
Python same solution as #142 Linked List Cycle II

https://leetcode.com/problems/find-the-duplicate-number/discuss/72852

* Lang:    python3
* Author:  zhuyinghua1203
* Votes:   22

In this problem, nums[a] = b can be seen as a.next = b, the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.

    def findDuplicate(self, nums):
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
