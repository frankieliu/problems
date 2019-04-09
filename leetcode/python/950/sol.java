
Simple Java Solution beats 99.83%

https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/248755

* Lang:    java
* Author:  icantcodeplshelp
* Votes:   0

```
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        if(n==0){
            return new int[]{};
        }
        Arrays.sort(deck);
        int result[] = new int[n];
        Queue<Integer> toput = new LinkedList();
        int j = 0;
        int i = 0;
        for(i=0;i<n;i+=2){
            if(i+1 < n)
                toput.add(i+1);
            result[i] = deck[j];
            j++;
        }
        if(i==n+1 && !toput.isEmpty()){
                toput.add(toput.remove());
        }
        while(j<n){
            int p = toput.remove();
            if(!toput.isEmpty()){
                toput.add(toput.remove());
            }
            result[p] = deck[j];
            j++;
        }
        return result;
    }
}
```
