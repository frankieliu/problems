
Java | 99 % | KMP pattern matching | O(m + n)

https://leetcode.com/problems/rotate-string/discuss/257182

* Lang:    java
* Author:  ripu23
* Votes:   0

The idea has been taken from [here](https://www.youtube.com/watch?v=GTJr8OvyEVQ).
```
class Solution {
    public boolean rotateString(String A, String B) {
    
        char[] a = (A + A).toCharArray();
        char[] b = B.toCharArray();
        int[] tmp = createTemp(b);
        int i = 0;
        int j = 0;
        while(i < a.length && j < b.length){
            if(a[i] == b[j]){
                i++;
                j++;
            }else{
                if(j != 0){
                    j = tmp[j - 1];
                }else{
                    i++;
                }
            }
        }
        return (j == b.length && A.length() == B.length()) ? true : false;
    }
    
    private int[] createTemp(char[] a){
        int[] temp = new int[a.length];
        int i = 0;
        for(int j = 1; j < a.length;){
            if(a[i] == a[j]){
                temp[j] = i + 1;
                i++;
                j++;
            }else{
                if(i != 0){
                    i = temp[i - 1];
                }else{
                    temp[j] = 0;
                    j++;
                }
            }
        }
        return temp;
    }
}
```
