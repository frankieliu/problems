
Memory limit exceeded in Arraylists Java

https://leetcode.com/problems/count-binary-substrings/discuss/112668

* Lang:    java
* Author:  psruthishalini
* Votes:   0

Hello All,
I am not sure why I am getting memory limit exceeded error in the following code. Can someone please explain. Thanks in advance.
```
class Solution {
    public int countBinarySubstrings(String s1) {
        List<String> subList = new ArrayList<>( );
             int counter=0;
            for(int i=0;i<(s1.length()-1);i++)
            {
                for(int j=i+2;j<=s1.length();j++)
                {
                    subList.add(s1.substring(i,j));

                }
            }
            for(String s2 : subList)
            {    int numofzero=0;
                 int numofone=0;
                for (int n = 0; n < s2.length(); n++)
                { if(s2.charAt(n)=='0')
                    numofzero=numofzero+1;
                    else
                       numofone=numofone+1;

                }
                int onechain = 0;
                int zerochain = 0;
                if(numofzero==numofone) {
                    for (int k = 0; k < s2.length()-1; k++) {

                        if ((s2.charAt(k) == '0')&&(s2.charAt(k+1) == '0'))
                            zerochain = zerochain + 1;
                        if ((s2.charAt(k) == '1')&&(s2.charAt(k+1) == '1'))
                            onechain = onechain + 1;
                    }
                    if ((numofzero == zerochain+1)&&(numofone == onechain+1))
                        counter=counter+1;

                }
            }
            return counter;
        
    }
}
````
