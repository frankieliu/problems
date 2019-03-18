
Bidirectional scan to skip multiple letters at one step

https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/254365

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

The keypoint of this solution: **speed up scan process by skip letters as much as possible, it is faster than one-step scanning when p is long.**
Instead of scaning letters one by one, when match failed I try to skip letters as many as possible like KMP algorithm (at this point).

Same as other solution, we maintain **start** and **end** two pointers  and a hashmap **counter**. And **scan forward** and **scan backward** alternately.
First we scan backward, because if we find a invalid word, we can jump all the words before it.

>**scan_backfoward(end)**:
Scan from end to start
* If counter[s[i]] == 0, jump all the words before it, and scan forward start from i + 1: **scan_foward(i + 1, end)**
* If all the letters matched, jump to **match_success(end)**

>**scan_forward(start, end)**:
Now we have matched from **start** to **end**, and need continue to match from **end** to **start+len(p)**:
* If mismatched jump to **match_failed(start, i)**
* If all mached jump to **match_success(start+len(p))**

>**match_success(end)**:
First add **start** index to results, and check if s[start] == s[end]. If matched, also add **start+1** to results , move pointers one step and repeat this process. when not matched, jump to **match_failed(start, end)**

>**match_failed(start, end)**:
There are two situations:
* If letter s[i] not in p, We skip all the words before it and scan backward start from i+1: **scan_backward(i + 1 + len(p))**
* If letter s[i] in p but use out, We find the first letter equal to it and scan forward start from this index+1: **scan_foward(index + 1, end + 1)**

```
    def findAnagrams(self, s: str, p: str) -> \'List[int]\':
        p_counter = Counter(p)
        n, k, self.res = len(s), len(p), []
        if k > n: return []

        def scan_backward(end):
            # reach the end
            if end > n:
                return
            # reset the counter
            self.counter = Counter(p_counter)
            # scan from end to start
            for i in range(end - k, end)[::-1]:
				# if not matched, skip all the words before i to speed up
                if self.counter[s[i]] == 0:
                    scan_forward(i + 1, end)
                    return
                else:
                    self.counter[s[i]] -= 1
			# jump to match_success
            match_success(end)
			
        def scan_forward(start, end):
			# reach the end
            if start + k > n:
                return
			# now we have matched from start to end, and need continue to match from end to start+len(p):
            for i in range(end, start + k):
				# if not in p or use out, jump to match_failed
                if self.counter[s[i]] == 0:
                    match_failed(start, i)
                    return
                else:
                    self.counter[s[i]] -= 1
            # jump to match_sucess
            match_success(start + k)

        def match_success(end):
            # add start index to results
            self.res.append(end - k)
            # if s[stat] == s[end], also add to results and move on, continue this process
            while end < len(s) and s[end] == s[end - k]:
                end += 1
                self.res.append(end - k)
            # reach the end
            if end == len(s):
                return
            # s[start] != s[end], jump to match_failed
            match_failed(end-k, end)

        def match_failed(start, end):
			# if s[i] not in p, we skip all the words before it and scan backward start from i+1
            if s[end] not in p_counter:
                scan_backward(end + k + 1)
            # letter s[i] in p but use out, we find the first letter equal to it and scan forward start from this index+1
            else:
                for i in range(start, end):
                    if s[i] != s[end]:
                        self.counter[s[i]] += 1
                    else:
                        scan_forward(i + 1, end + 1)
                        return

        scan_backward(k)
        return self.res
```
 

