
[Java] 78% 180ms Constant Lookup, No Binary Search

https://leetcode.com/problems/online-election/discuss/229920

* Lang:    java
* Author:  ChakuRam
* Votes:   0

class TopVotedCandidate {
        private Map <Integer,Integer> winner;

    private Map <Integer,Integer> winner;

    public TopVotedCandidate(int[] persons, int[] times) {
        Map<Integer,Integer> votes = new HashMap<>();
        winner = new HashMap<>();
        int maxVotes = -1, leading = -1;
        
        for(int i=0;i<persons.length;++i){
            
            votes.put(persons[i],votes.getOrDefault(persons[i],0)+1);
            
            if(votes.get(persons[i])>=maxVotes){    // If tie, update with new
                maxVotes = votes.get(persons[i]);
                leading = persons[i];
            }
            winner.put(times[i],leading);
        }
        
    }
    // clever trick to floor t, instead of binary search. We need to floor t because..
	// Time lookup (t) may be 14s when inputs are only 10s & 15s. so winner at 10s will be winner at 14s
	
    public int q(int t) {
        while(!winner.containsKey(t)) 
			t--;                                        
        return winner.get(t);
    }
}

