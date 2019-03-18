
99ms Python O(kmn) Solution

https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669

* Lang:    python3
* Author:  GavinCode
* Votes:   12

The idea comes from [https://leetcode.com/discuss/20151/an-o-n-solution-with-detailed-explanation]

Using a counter and a sliding window, we push the window from left to right, counting the number of valid words in the window. When the number of a word in the window is more than the times it appears in **words** or we meet a invalid word, push the window.

    class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):
		if len(words) == 0:
			return []
		# initialize d, l, ans
		l = len(words[0])
		d = {}
		for w in words:
			if w in d:
				d[w] += 1
			else:
				d[w] = 1
		i = 0
		ans = []

		# sliding window(s)
		for k in range(l):
			left = k
			subd = {}
			count = 0
			for j in xrange(k, len(s)-l+1, l):
				tword = s[j:j+l]
				# valid word
				if tword in d:
					if tword in subd:
						subd[tword] += 1
					else:
						subd[tword] = 1
					count += 1
					while subd[tword] > d[tword]:
						subd[s[left:left+l]] -= 1
						left += l
						count -= 1
					if count == len(words):
						ans.append(left)
				# not valid
				else:
					left = j + l
					subd = {}
					count = 0

		return ans

Assuming we have k words in **words**, and there are m substrings in the string, the complexity is O(kmn) because we need to adjust the window when more valid words are found.

This solution runs 99ms on OJ.
