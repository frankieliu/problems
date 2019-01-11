"""31. Next Permutation
Medium

1307

377

Favorite

Share

Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Accepted
200.4K
Submissions
673.2K
"""

class Solution:
    def nextPermutation(self, n):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the first n[i-1] < n[i]
        j = -1
        for i in range(len(n)-1, 0, -1):
            if n[i-1] < n[i]:
                j = i-1
                break

        print("reverse found at:", j)

        if j == -1:
            # reverse the numbers:
            self.reverse(n, 0, len(n)-1)
            return

        # replace with smallest element greater than n[i-1]
        for i in range(len(n)-1, j, -1):
            if n[j] < n[i]:
                n[j], n[i] = n[i], n[j]
                self.reverse(n, j+1, len(n)-1)

                return
        return

    def reverse(self, n, i, j):
        p1 = i
        p2 = j
        while p1 < p2:
            n[p1], n[p2] = n[p2], n[p1]
            p1 += 1
            p2 -= 1

s = Solution()
n = [1, 2, 3]
s.nextPermutation(n)
print(n)
