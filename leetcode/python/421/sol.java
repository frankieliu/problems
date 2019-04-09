
Java Solution

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91104

* Lang:    java
* Author:  fabrizio3
* Votes:   0

```
public int findMaximumXOR(int[] nums) {
		
	int mostSignificantDifferentBit = 0;
	
	List<Integer> ones = new ArrayList<>();
	List<Integer> zeroes = new ArrayList<>();
	for(int i=31;i>=0 && (ones.isEmpty() || zeroes.isEmpty()); i--) {
		zeroes.clear();
		ones.clear();
		for(int n: nums) {
			if((n>>i & 1) == 1) {
				ones.add(n);
			} else {
				zeroes.add(n);
			}
		}
		mostSignificantDifferentBit=i;
	}
	
	return maxXorRec(ones, zeroes, mostSignificantDifferentBit-1);
}
	
private int maxXorRec(List<Integer> ones, List<Integer> zeroes, int nextBitToProcess){
	if(ones.size()==1 && zeroes.size()==1) return ones.get(0) ^ zeroes.get(0);
	List<Integer> onesOnes = new ArrayList<>();
	List<Integer> onesZeroes = new ArrayList<>();
	List<Integer> zeroesOnes = new ArrayList<>();
	List<Integer> zeroesZeroes = new ArrayList<>();

	for(int num: ones) {
		if(((num>>nextBitToProcess) & 1) == 1) onesOnes.add(num);
		else onesZeroes.add(num);
	}

	for(int num: zeroes){
		if(((num>>nextBitToProcess) & 1) == 1) zeroesOnes.add(num);
		else zeroesZeroes.add(num);
	}

	int max = 0;
	if(onesOnes.size()!=0 && zeroesZeroes.size()!=0) max = maxXorRec(onesOnes, zeroesZeroes, nextBitToProcess-1);
	if(onesZeroes.size()!=0 && zeroesOnes.size()!=0) max = Math.max(max, maxXorRec(onesZeroes,zeroesOnes,nextBitToProcess-1));
	return max;
}
```
