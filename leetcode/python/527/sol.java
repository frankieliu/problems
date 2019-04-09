
Just Brute-Force

https://leetcode.com/problems/word-abbreviation/discuss/99818

* Lang:    java
* Author:  nijixuchao
* Votes:   1

Just brute-force, and reuse some code, nothing special...
```
public class Solution {
    public List<String> wordsAbbreviation(List<String> dict) {
        int n = dict.size();
        List<String> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int prefix = 1;
            String abbr = abbrPrefix(dict.get(i), prefix);
            while (conflict(abbr, dict, i)) {
                prefix++;
                abbr = abbrPrefix(dict.get(i), prefix);
            }
            res.add(abbr);
        }
        return res;
    }
    
    private String abbrPrefix(String s, int prefix) {
        if (prefix + 2 >= s.length()) {
            return s;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(s.substring(0, prefix));
        sb.append(s.length() - prefix - 1);
        sb.append(s.charAt(s.length() - 1));
        return sb.toString();
    }
    
    private boolean conflict(String abbr, List<String> dict, int except) {
        for (int i = 0; i < dict.size(); i++) {
            if (i != except && isValidAbbreviation(dict.get(i), abbr)) {
                return true;
            }
        }
        return false;
    }
    
    private boolean isValidAbbreviation(String word, String abbr) {
        int i = 0, j = 0;
        int num = 0;
        while (i < word.length() && j < abbr.length()) {
            char a = abbr.charAt(j);
            if (Character.isDigit(a)) {
                num = num * 10 + a - '0';
                j++;
            } else {
                i += num;
                num = 0;
                if (i >= word.length() || word.charAt(i) != a) {
                    return false;
                }
                i++;
                j++;
            }
        }
        i += num;
        return i == word.length() && j == abbr.length();
    }
}
```
