
Addition Simulator Solution, clear and fast [11 lines]

https://leetcode.com/problems/next-closest-time/discuss/248657

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

Instead of traversing by **minutes** or **allowed digits**, I tried to find out the next valid time directly.
Here we can treat allowed digits as another form of number representation, which named as **time-number**, and build an **Addition Simulator**.

For example, 18:39 has a sorted digits spcae [1,3,8,9], and tried to find next valid **time-number**.
Here is the rule:
If next digit is valid, just return it. 
If next digit is not valid or reach the end, set it to the first digit and carry to high-position (which means **carry** in addition).

18:3**9** reach the end and carry to high-position -> 18:3**1**
18:**3**1 chang to next digit -> 18:**8**1
18:**8**1 is not valid, set it to first digit and carry to high-position -> 18:**1**1
1**8**:11  chang to next digit -> 1**9**:11
1**9**:11 is valid and return it

```
def nextClosestTime(self, time: str) -> str:
	words = sorted(list(set(time[:2] + time[3:])))
	res = list(time[:2] + time[3:])
	
	for idx in range(4)[::-1]:
		next_idx = words.index(res[idx]) + 1
		if next_idx < len(words):
			# change to the next digit
			res[idx] = words[next_idx]
			hour, minute = divmod(int(\'\'.join(res)), 100)
			# if it is valid time, just return it
			if hour < 24 and minute < 60:
				return \'\'.join(res[:2]) + \':\' + \'\'.join(res[2:])
		# back to the first digit, and carry to high-position
		res[idx] = words[0]
	return \'\'.join(res[:2]) + \':\' + \'\'.join(res[2:])
```


Time Complexity Analysis:
Traversing by minutes:  O(24 * 60) possible times 
Traversing by allowed digits: O(4^4) possible times
Find next valid time: at most O(4) possible times
