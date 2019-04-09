
Simple Python Code

https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234511

* Lang:    python3
* Author:  rahulprinci
* Votes:   1

Logic-1.Convert list of integers into a number 
				Ex-if A =[\'1\',\'2\',\'3\'] =>1x100+2x10+3x1 =123
			2.Perform addition of A and K
			3.Convert back the result into List
Time Complexity-O(n)
```class Solution:
    def addToArrayForm(self, A: \'List[int]\', K: \'int\') -> \'List[int]\':
        j=0
        count=0
        for i in A:
            j=j+(i*(10**(len(A)-1-count)))
            count= count+1
        return ([int(x) for x in str(j+ K)])
		
