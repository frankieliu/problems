
4 lines Python solution

https://leetcode.com/problems/repeated-dna-sequences/discuss/53892

* Lang:    python3
* Author:  alizee56
* Votes:   18

I use a defauldict to initialize as 0 the dictionary of integers, then I check the dictionary for substrings seen more than once.

    class Solution:
        # @param s, a string
        # @return a list of strings
        def findRepeatedDnaSequences(self, s):
            sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
            for i in range(len(s)):
                sequences[s[i:i+10]] += 1#add 1 to the count
            return [key for key, value in sequences.iteritems() if value > 1] #extract the relevant keys
