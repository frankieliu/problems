
Share my JAVA AC solution and my thoughts

https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/92853

* Lang:    java
* Author:  KnightY
* Votes:   4

```
public int numberOfArithmeticSlices(int[] A) {
        if(A==null||A.length<3) return 0;
        List<Map<Integer,Integer>> list=new ArrayList<Map<Integer,Integer>>();
        int res=0;
        for(int i=1;i<A.length;i++){
            Map<Integer,Integer> map=new HashMap<Integer,Integer>();
            for(int j=0;j<i;j++){
                if((long)A[i]-(long)A[j]>Integer.MAX_VALUE) continue;
                if((long)A[i]-(long)A[j]<Integer.MIN_VALUE) continue;
                int dif=A[i]-A[j];
                if(j==0){
                    map.put(dif,1);
                    continue;
                }
                Map<Integer,Integer> temp=list.get(j-1);
                int sum=0;
                if(temp.containsKey(dif)){
                    sum=temp.get(dif);
                }
                if(map.containsKey(dif)){
                    map.put(dif,map.get(dif)+sum+1);
                }else{
                    map.put(dif,sum+1);
                }
                res+=sum;
            }
            list.add(map);
        }
        return res;
    }
```
It seems that there is no better way to solve this problem using O(N^2) space and time. If you have better algorithm, please share your thoughts or solution, thanks!

I have viewed all four posts( at least there are four posts when I am still busy typing mine), and everyone seems to have the same issue facing TLE or MLE or both. Well, for me, I have encountered both.

Since nobody has posted java solution, I will share my ways of tackling this problem.

I will skip the logic and algorithms here, since everybody is doing it the same way, using DP. For each element, store all possible difference and its number of arithmetic sequences( including 2 element sequence). 

At first, I was using Map<Long,Integer> instead of Map<Integer,Integer> considering subtraction of two integers could result in overflow. But later I realized if the result is bigger than the max value of integer or smaller than the min value of integer, there is no way to have a valid a 3rd integer element to form a arithmetic sequence. So by adding two if()*continue, and thus replacing Map<Long,Integer> to Map<Integer,Integer> it can save both time and memory. After doing this, my code can pass the judge about 4 out of 5 times, which means it can still have TLE or MLE sometimes. Then I modified the outer loop's parameter i to start from 1 instead of 0 and added if(j==0) statement to do less map operations for every j==0 case. And now it goes through every time! (Well, by saying every time, I mean I submitted 5 times in a row and they all went through.)

I believe the first change is the main cause to help my code get through, and the second change is just the minor. Hope these can give you guys some hints and help, please do share your plans of reducing either time or space here if you have. 
Happy coding!
