In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1160.find-words-that-can-be-formed-by-characters.algorithms.json

[Easy Explained] Simple Java Check all char count

https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/361004

* Lang:    python
* Author:  JatinYadav
* Votes:   11

```

    public static int countCharacters(String[] words, String chars) {
        int count = 0;
        int[] seen = new int[26];
		//Count char of Chars String
        for (char c : chars.toCharArray())
            seen[c - \'a\']++;
		// Comparing each word in words
        for (String word : words) {
			// simple making copy of seen arr
            int[] tSeen = Arrays.copyOf(seen, seen.length); 
            int Tcount = 0;
            for (char c : word.toCharArray()) {
                if (tSeen[c - \'a\'] > 0) {
                    tSeen[c - \'a\']--;
                    Tcount++;
                }
            }
            if (Tcount == word.length())
                count += Tcount;
        }
        return count;
    }

```
