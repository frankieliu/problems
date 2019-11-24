In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1167.minimum-cost-to-connect-sticks.algorithms.json

No PriorityQueue(MinHeap) just Sort exactly once (with detailed Explanation)

https://leetcode.com/problems/minimum-cost-to-connect-sticks/discuss/365913

* Lang:    python
* Author:  darup
* Votes:   9

You will find a quick solution using priority queue, but in an interview when you are asked this question and you come up with a solution that beats the best data structure (heap) for this problem. How much impact would that make! :) The idea is simple but very efficient. Also, if a priority queue is used, the approximate runtime complexity is 4 * O(log(N!)) ~ O(log(N!)) which is more than O(NlogN) where as the suggested approach gives a proper runtime complexity of O(NlogN).

**Note**: Mathematically log(N!) < NlogN and 4 * log(N!) > NlogN. But since the runtime complexity is represented in O notation, constants are removed. My intention is to say that the runtime (measured in time) will be more when using a heap compared to just sorting once.

The main idea is to get the smallest sticks and combine. Do we really need a heap to do that! A simple sort should do it. Coming to the sum of sticks: the smaller sticks result in smaller sum and as the stick size increases the sum of those sticks also increases. So, if you notice correctly, the sum values are always in increasing order, indirectly saying the sum list is already sorted. Then why use a heap! Just store the results in a sequence. I tried to explain below how we can achieve the result in a greedy fashion without using any heap.
The idea is to sort the initial array and store results (sum of two sticks) back into the same array. But putting back the results should be done in correct way. Lets take an example:
[1 8 3 5 4 6]

First it is sorted
[1 3 4 5 6 8] - This takes exactly O(NlogN)

My set of variables to store some information:
right = 0 // to store the index from where we start looking for sticks
numSticks = 6 // number of Sticks
left = 0 // the first index where we should look for the stored result values (when we have result values)
numResults = 0 // number of results computed, initially 0 since we did not compute any sum
result = 0// Store the final result.

Basically the array is divided in two sets. First set is the input values i.e., [right, numSticks). Note that numSticks is exclusive. Second set is the results(sum of sticks) i.e., [left, numResults). Note that numResults is exclusive.

Initially
Array: [1 3 4 5 6 8] - Sorted
InputSet: [1 3 4 5 6 8] - [right, numSticks) - [0, 6)
ResultSet : [] - [left, numResults) - [0, 0)

Since no numbers in the ResultSet take first two numbers from InputSet. First two because the list is sorted. So the first two nums are 1 & 3. Add them and store it in Result set. Also update the input set and add the sum to result.

Array: [4 3 4 5 6 8]
InputSet: [4 5 6 8] - [right, numSticks) - [2, 6)
ResultSet : [4] - [left, numResults) - [0, 1)
result = 0 + 4 = 4
The value in index 1 is useless now because it has been used to compute a sum.

Now from the updated sets choose the first two small numbers. This can be easily done by comparing the first numbers form the two sets and choosing the smallest. Here 4 from InputSet and another 4 from ResultSet. Sum is 8 and update both lists. Also add the sum to result.

Array: [4 8 4 5 6 8]
InputSet: [5 6 8] - [right, numSticks) - [3, 6)
ResultSet : [8] - [left, numResults) - [1, 2)
result = 4 + 8 = 12
Again we don\'t care about the values that we have already used. Example: 4 in index 0 and index 2

Now again choose the smallest from the updated sets. This time both numbers are from input set i.e., 5 and 6. Sum is 11. Update input and result set. Also add the sum to result.

Array: [4 8 11 5 6 8]
InputSet: [8] - [right, numSticks) - [5, 6)
ResultSet : [8, 11] - [left, numResults) - [1, 3)
result = 12 + 11 = 23

Choose smallest from the updated sets. 8 from InputSet and another 8 from ResultSet. Sum is 16. Update both sets. Also add the sum to result.

Array: [4 8 11 16 6 8]
InputSet: [] - [right, numSticks) - [6, 6)
ResultSet : [11, 16] - [left, numResults) - [2, 4)
result = 23 + 16 = 39

Choose smallest from the updated sets. No number in InputSet. So choose 11 and 16. Result is 27. Update sets. Also add the sum to result.

Array: [4 8 11 16 27 8]
InputSet: [] - [right, numSticks) - [6, 6)
ResultSet : [27] - [left, numResults) - [4, 5)
result = 39 + 27 = 66

Only one number is left. Stop the loop and return result.

C++ code
```
class Solution {
private:
    int left = 0, right = 0, numSticks, numResults = 0;
    // Gets the minimum from InputSet and ResultSet
    bool getMin(vector<int>& sticks, int &num) {
        // check if there are numbers available from InputSet and ResultSet
        bool f = right < numSticks, s = left < numResults;
        // If number is available from both sets, choose the smallest
        if (f && s) num = (sticks[left] <= sticks[right]) ? sticks[left++] : sticks[right++];
        // If number is available from InputSet only
        else if (f) num = sticks[right++];
        // If number is available from ResultSet only
        else if (s) num = sticks[left++];
        return f || s; // Returns result saying if we could find a number from any one of the Sets.
    }
public:
    int connectSticks(vector<int>& sticks) {
        numSticks = sticks.size();
        sort(sticks.begin(), sticks.end()); // Initial sort
        int result = 0, first, second; // Result and place holders to get the smallest two numbers.
        // Continue till you can get two numbers every time from the Sets.
        while (getMin(sticks, first) && getMin(sticks, second))
            result += sticks[numResults++] = first + second; // Store the sum back in the ResultSet
        return result;
    }
};
```

Java Code
```
class Solution {
    int left = 0, right = 0, numSticks, numResults = 0, num;
    // Gets the minimum from InputSet and ResultSet
    private boolean getMin(int[] sticks) {
        // check if there are numbers available from InputSet and ResultSet
        boolean f = right < numSticks, s = left < numResults;
        // If number is available from both sets, choose the smallest
        if (f && s) num = (sticks[left] <= sticks[right]) ? sticks[left++] : sticks[right++];
        // If number is available from InputSet only
        else if (f) num = sticks[right++];
        // If number is available from ResultSet only
        else if (s) num = sticks[left++];
        return f || s; // Returns result saying if we could find a number from any one of the Sets.
    }
    
    public int connectSticks(int[] sticks) {
        numSticks = sticks.length;
        Arrays.sort(sticks); // Initial sort
        int result = 0, first, second; // Result and place holders to get the smallest two numbers.
        // Continue till you can get two numbers every time from the Sets.
        while (true) {
            if (!getMin(sticks)) break;
            first = num;
            if (!getMin(sticks)) break;
            second = num;
            result += sticks[numResults++] = first + second; // Store the sum back in the ResultSet
        }
        return result;
    }
}
```

The major difference is that pushing and poping values on a priority queue (min heap) takes O(logN) time but using this approach it is reduced to O(1) time. Hence the major difference in time.

Runtime Complexity: O(NlogN)
Space Complexity: O(1) if you can use the same input array or O(N) if you can\'t use the input array and have to create a copy of it.
