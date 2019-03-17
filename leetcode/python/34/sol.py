
Search for the position target-0.5 and target+0.5, a simple python code with a little trick

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14713

* Lang:    python3
* Author:  tusizi
* Votes:   15

    class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, arr, target):
        start = self.binary_search(arr, target-0.5)
        if arr[start] != target:
            return [-1, -1]
        arr.append(0)
        end = self.binary_search(arr, target+0.5)-1
        return [start, end]

    def binary_search(self, arr, target):
        start, end = 0, len(arr)-1
        while start < end:
            mid = (start+end)//2
            if target < arr[mid]:
                end = mid
            else:
                start = mid+1
        return start

for search the target+0.5 position we add something whatever to the list end
 to get the right position for the edge case

take ([0,1,2,3,4,5], 5) for example:

we append 0 to the list end

[0,1,2,3,4,5,0]

[4,5,0]# start now is 4, end is 6, mid is 5,  start = mid+1 = 6, end the while loop

finally we get the 5.5 position == start == 6
