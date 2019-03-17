
Python 56 ms Time O(N*M) Space O(1)

https://leetcode.com/problems/implement-strstr/discuss/13255

* Lang:    python3
* Author:  luanmaova
* Votes:   25

Do we need to really use KMP in the interview? I just had a few interviews but personally I really can not remember those fantastic algorithms in that short period of time in pressure. Maybe I was nervous and needed more programming practice..


    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1
