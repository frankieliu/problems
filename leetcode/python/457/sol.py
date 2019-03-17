
Ugly fast/slow pointer Python solution. O(n) time O(1) space

https://leetcode.com/problems/circular-array-loop/discuss/94224

* Lang:    python3
* Author:  whglamrock
* Votes:   0

Use fast/slow pointer to detect loop, just like we did for the linked list.
Also, if we don't find a loop, mark all visited elements zero.

'''

    def circularArrayLoop(self, nums):

        if not nums or len(nums) < 2: return False
        
        for i in xrange(len(nums)):
            
            if nums[i] == 0:
                continue
            if nums[i] > 0:
                direction = 1
            else:
                direction = -1
            flag = True  # check is the direction remains unchanged
            slow, fast = i, (i + nums[i]) % len(nums)
            visited = 1
            
            while slow != fast and flag and visited < len(nums):
                nextslow = (slow + nums[slow]) % len(nums)
                if direction * nums[slow] < 0:
                    flag = False
                    break
                slow = nextslow
                nextfast = (fast + nums[fast]) % len(nums)
                if direction * nums[fast] < 0:
                    flag = False
                    break
                fast = nextfast
                nextfast = (fast + nums[fast]) % len(nums)
                if direction * nums[fast] < 0:
                    flag = False
                    break
                fast = nextfast
                visited += 1
               
            # fast != (fast + nums[fast]) % len(nums) checks for 1 element loop
            # flag checks if direction's been changed
            if slow == fast and flag and fast != (fast + nums[fast]) % len(nums):
                return True
            else:
                j = i
                while j != fast and visited > 0:
                    nums[j] = 0
                    j = (j + nums[j]) % len(nums)
                    visited -= 1
                nums[j] = 0
                    
        return False
'''
