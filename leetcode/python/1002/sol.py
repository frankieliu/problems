
Python Explained (no Counter, intuitive solution)

https://leetcode.com/problems/find-common-characters/discuss/248410

* Lang:    python3
* Author:  mikqs
* Votes:   1

**Approach**
1) Initialize a dictionary dict1 with letter counts from word#1
2) Compare letters in dict1 with word#2: add letters in common to dict2 while reducing the count in dict1 to account for duplicates
3) Clear dict1
4) Compare letters in dict2 with word#3 in the same fashion
5) Clear dict2
6) Repeat for next words, alternating between filling/clearing dict1/2
7) Return result from the appropriate dictionary

Will appreciate if you guys can suggest more condensed code with this logic.

Cheers

**Solution**
```
    def commonChars(self, A: List[str]) -> List[str]:
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        k = 0
        
        for letter in A[0]:
            dict1[letter] += 1
        
        for word in A[1:]:
            if k%2 == 0:
                for letter in word:
                    if dict1[letter]:
                        dict2[letter] += 1
                        dict1[letter] -= 1
                dict1.clear()
            else:
                for letter in word:
                    if dict2[letter]:
                        dict1[letter] += 1
                        dict2[letter] -= 1
                dict2.clear()
            k += 1
        
        if k%2 == 0:
            result = [letter for l,cnt in dict1.items() for letter in l*cnt]
        else:
            result = [letter for l,cnt in dict2.items() for letter in l*cnt]

        return result
```
