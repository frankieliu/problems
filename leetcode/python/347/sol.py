
1-line Python Solution using Counter with explanation

https://leetcode.com/problems/top-k-frequent-elements/discuss/81639

* Lang:    python3
* Author:  myliu
* Votes:   38

    import collections
    
    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            # Use Counter to extract the top k frequent elements
            # most_common(k) return a list of tuples, where the first item of the tuple is the element,
            # and the second item of the tuple is the count
            # Thus, the built-in zip function could be used to extract the first item from the tuples
            return zip(*collections.Counter(nums).most_common(k))[0]
