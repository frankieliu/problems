In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1056.confusing-number.algorithms.json

Java Solution using HashMap - Similar to 246. Strobogrammatic Number

https://leetcode.com/problems/confusing-number/discuss/303832

* Lang:    python
* Author:  Makubex74
* Votes:   7

* Store <digit, inverted digit> as <K, V> in HashMap.
* Keep dividing current number by 10 and check individual digit to see if it exists in the HashMap or return false if not found.
* Construct new number by multiplying new number by 10 each time and adding the inverted digit for the current remainder value.
* Check if original number and new number are the same.
```
class Solution {
    public boolean confusingNumber(int N) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(6, 9);
        map.put(9, 6);
        map.put(0, 0);
        map.put(1, 1);
        map.put(8, 8); 
        int newNum = 0;
        int x = N;
        while (x != 0) {
            int remainder = x % 10;
            if (!map.containsKey(remainder)) 
                return false;
            if(newNum > Integer.MAX_VALUE/10)
                return false;
            newNum = newNum * 10 + map.get(remainder);
            x /= 10;
        }    
        return N == newNum? false: true;
    }
}
```

