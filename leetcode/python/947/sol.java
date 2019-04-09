
java union find with Stone as a class  holding  it's index and it's parent index

https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/245063

* Lang:    java
* Author:  AmareshB
* Votes:   0

```
class Stone {
    int index;
    int parentIndex;
    int rank;
    Stone(int index, int parentIndex, int rank) {
        this.index = index;
        this.parentIndex = parentIndex;
        this.rank = rank;
    }
}

class Solution {
    public int removeStones(int[][] stones) {Map<Integer, Stone> stone_parent = new HashMap<>();
        for(int i = 0; i < stones.length; i++) {
            stone_parent.put(i, new Stone(i,i,0));
        }

        for(int i = 0; i < stones.length; i++) {
            for(int j = 0; j < stones.length; j++) {
                if(stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    union(stone_parent, stone_parent.get(i), stone_parent.get(j));
                }
            }
        }

        Set<Integer> roots = new HashSet<>();

        for(int i = 0; i < stones.length; i++) {
            roots.add(find(stone_parent, stone_parent.get(i)).parentIndex);
        }

        return stones.length - roots.size();
    }

    public void union (Map<Integer, Stone> stone_parent, Stone stone1, Stone stone2) {
       Stone Parent1 = find(stone_parent, stone1);
        Stone Parent2 = find(stone_parent, stone2);
        if(Parent1.index == Parent2.index) {
            return;
        }
        if(Parent1.rank >= Parent2.rank) {
            Parent1.rank = Parent1.rank == Parent2.rank ? Parent1.rank +1: Parent1.rank;
            Parent2.parentIndex = Parent1.index;
        } else {
            Parent2.rank ++;
            Parent1.parentIndex = Parent2.parentIndex;
        }
    }

    public Stone find(Map<Integer, Stone> stone_parent, Stone stone){
        if(stone.index == stone.parentIndex) {
           return stone_parent.get(stone.parentIndex);
        }

        stone.parentIndex = find(stone_parent, stone_parent.get(stone.parentIndex)).index;
        return stone_parent.get(stone.parentIndex);
    }
}
```
