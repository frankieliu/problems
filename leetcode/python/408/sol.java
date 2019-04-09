
Simple & easy java solution

https://leetcode.com/problems/valid-word-abbreviation/discuss/89566

* Lang:    java
* Author:  powerstar
* Votes:   0

```
public boolean validWordAbbreviation(String word, String abbr) {
        if(word == null && abbr == null) {
            return true;
        }
        
        if(word == null || abbr == null) {
            return false;
        }
        
        if(word.isEmpty() && abbr.isEmpty()) {
            return true;
        }
        
        if(word.isEmpty() || abbr.isEmpty()) {
            return false;
        }

        int pos = 0;
        
        for(int i = 0; i < abbr.length(); i++) {
            // Safe gaurd pos, it should never be greater
            // than word.length() at the beginning of the loop
            if(pos >= word.length()) {
                return false;
            }
            char c = abbr.charAt(i);
            if(Character.isLetter(c)) {
                // If same character, we are fine
                if(word.charAt(pos) == c) {
                    pos++;
                } else {
                    // If different character at
                    // the pos we are expecting
                    // return false
                    return false;
                }
            } else if (Character.isDigit(c)) {
                int num = c - '0';
                // If first digit is 0 then false
                if(num == 0) {
                    return false;
                }
                // Compute the whole number
                while(i + 1 < abbr.length() && Character.isDigit(abbr.charAt(i + 1))){
                    num = num * 10 + (abbr.charAt(++i) - '0');
                }
                // Increment pos
                pos += num;
            }
        }
        return pos == word.length();
    }
```
