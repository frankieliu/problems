
Java simple solution. 3ms beats 100%

https://leetcode.com/problems/sentence-similarity/discuss/229917

* Lang:    java
* Author:  Aevil1
* Votes:   0

```
class Solution {

    public boolean isSimilar(String word1, String word2, String[][] pairs)
{
	if (word1.equals(word2))
		return true;
	
	for (int i = 0; i < pairs.length; i++)
	{
if (Arrays.asList(pairs[i]).contains(word1) && Arrays.asList(pairs[i]).contains(word2))
{
	return true;
}
}

return false;
}

    public boolean areSentencesSimilar(String[] words1, String[] words2, String[][] pairs) {
        	if (words1.length != words2.length)
		return false;

	if (words1.length == 0)
		return true;


	for (int i = 0; i < words1.length; i++)
	{
		if (!isSimilar(words1[i], words2[i], pairs))
		{
			return false;
}
}

return true;
    }
}
```


