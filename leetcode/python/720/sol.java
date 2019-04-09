
[Java] Heap Solution (lol)

https://leetcode.com/problems/longest-word-in-dictionary/discuss/235159

* Lang:    java
* Author:  arcan770077f
* Votes:   0

```
import java.util.*;

class MyComparator implements Comparator<String> {
    @Override
    public int compare(String a, String b) {
        // judge by lexicographical order
        if (a.length() == b.length())
            return a.compareTo(b);
        
        // else by length
        return b.length() - a.length();
    }
}

class Solution {
    public String longestWord(String[] words) {
        if (words.length == 0)
            return "";
        
        // hashset words for quick lookups
        Set<String> set = new HashSet<>();
        for (String word : words)
            set.add(word);
        
        // check if you can build them through other words in the set (one char at a time)
        List<String> buildable = new ArrayList<>();
        for (String word : words) {
            // assume good
            buildable.add(word);
            // try to prove wrong
            for (int i = word.length() - 1; i > 0; i--) {
                if (!set.contains(word.substring(0, i)))
                    buildable.remove(word);
            }
        }
        
        // pick top candidates
        PriorityQueue<String> lengthHeap = new PriorityQueue<>(words.length, new MyComparator());
        for (String word : buildable)
            lengthHeap.add(word);
        
        return lengthHeap.poll(); 
    }
}
```
