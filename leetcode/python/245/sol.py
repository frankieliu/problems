
[8 lines] one pass concise python solution, beat 100%

https://leetcode.com/problems/shortest-word-distance-iii/discuss/249879

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

Instead of using two-pointer, just use one pointer to represent both words, and same words case is also included.
   
    def shortestWordDistance(self, words: \'List[str]\', word1: str, word2: str) -> int:
        cur_word, idx, min_dist = None, 0, len(words)
        for i, w in enumerate(words):
            if w not in (word1, word2):
                continue
            if cur_word and (word1 == word2 or w != cur_word):
                min_dist = min(min_dist, i - idx)
            cur_word, idx = w, i
        return min_dist
	
	
Time Complexity: O(n)
Space Complexity: O(1)
