
Share my O(n) C++ solution with proof and explanation

https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/240086

* Lang:    cpp
* Author:  KJer
* Votes:   2

---
## 1. Problem

---
In an array ```A``` containing only 0s and 1s, a *```K```*-bit flip consists of choosing a (contiguous) subarray of length ```K``` and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of ```K```-bit flips required so that there is no 0 in the array.  If it is not possible, return ```-1```.

**Example 1:**
```
Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
```

**Example 2:**
```
Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can\'t make the array become [1,1,1].
```

**Example 3:**
```
Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
```
**Note:**
* 1 <= A.length <= 30000
* 1 <= K <= A.length

---
## 2. Thinking process

---
#### 2.1 Analysis

---

The problem is complicated at first glance.
As a ```K```-bit flip is applied on a length-K contiguous subarray of A, if the size of array A is **N**, and the **subarray starts at index i (0 \u2264 i \u2264 N- K)**, **i** can be used for specifying such a flip.

In this way, 
>#### **A flip sequence can be defined by an index sequence**.

In **Example 3**, 
```
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
```
the sequence of index is **{0, 4, 5}**.

---
#### 2.2 Order invariance

---
In **Example 3**, if the sequence of index is changed to **{4, 0, 5}**, what will happen?
```
Flip A[4],A[5],A[6]: A becomes [0,0,0,1,1,0,0,0]
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
```
The final result is as same as the one with sequence **{0, 4, 5}**!

---
**Property A:**
>#### **The result is independent of the order of the flip sequence.**


**Proof:**

If the flip sequence is **{a0, a1, a2, ... , ap}**, and the original array A is changed to A\',

For **any A[i] (0 \u2264 i \u2264 N - K)** in A, if the **total count of flip on A[i] is c[i]**, when the order of flip sequence changes, **c[i] won\'t change**.

That is to say

>#### The corresponding A\'[i] and the array A\' will not change. Proved!

---
#### 2.3 Parity invariance

---
In **Example 3**, if the sequence of index is changed to **{0, 1, 1, 4, 4, 4, 5}**, what will happen?
```
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[1],A[2],A[3]: A becomes [1,0,0,0,0,1,1,0]
Flip A[1],A[2],A[3]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
```
The final result is as same as the one with sequence **{0, 4, 5}**!

---
**Property B:**
>#### In the flip sequence, the result is **ONLY** related to the **parity of count of index\'s appearance**.

**Proof:**
If an **index p (0 \u2264 i \u2264 N - K) appears in the flip sequence q times**, and the **total count of flip on A[i] is c[i]**, 
**q will be added to the total count of flip c[i] (p \u2264 i < p + K).**

In a single flip,
>#### If A[i] = 0, it will be flipped to 1.
>#### If A[i] = 1, it will be flipped to 0.

So, after **q flips on index p**,
>#### If q is even , A[i] will keep its value.
>#### If q is odd , A[i] will be flipped.

---
#### 2.4 Minimization

---
The problem is to find the minimum size of the flip sequence that removes all zeros in A.

If such a flip sequence exists, 

by applying **Property A in Section 2.2**,
>#### The sequence can be **sorted by index in ascending order**.

After sorting, in order to **minimize the sequence\'s size**, by applying **Property B in Section 2.3**,

>#### There are only 2 choices on each index - **appear ONLY once or don\'t appear**.

Now, every index in the sequence is **unique**.

---
#### 2.5 Generate the sequence

---
As mentioned in Section 2.4, every index sequence **S** can be simplified to a new sequence **S\'**.

>#### All indexes in S\' are **in ascending order and unique**.

As indexes are in ascending order, 
> #### **The later flip with larger index can\'t change the value at current index.**

which means,

If **A[0] = 0**, and **0 is NOT in the sequence**, **A[0] MUST equals to 0 in the final result**.

If **A[0] = 1**, and **0 is in the sequence**, **A[0] MUST equals to 0 in the final result**.

---
Since **the result MUST contains no 0**, when **processing index 0**

* **If A[0] = 0**, **0 MUST be in the sequence**, **A[0], A[1], ..., A[K - 1]** is **flipped**.
* **If A[0] = 1**, **0 MUST NOT be in the sequence**, **A[0], A[1], ..., A[K - 1]** is **NOT flipped**.

**After index 0 is processed, index 1 should be processed similarly**.

---
## 3. Algorithm

---
#### 3.1 Trivial solution

---
As discussed in Section 2.5, the algorithm is a dual-cycle.

**Initially, the total flip count c equals to 0.**
- **Outer Loop:** iterate **index i** from **0 to N - K**.
   - If **A[i] = 0**, 
       - **Inner Loop:** **flip A[i], A[i + 1], ..., A[i + K - 1]**. 
       - **Set c = c + 1**.
   - Else, ignore.
- **After processing**, check the **remain elements in A**,
  - If **all elements are 1**, **return c**.
  - **Else**, **return -1**.

For example,
```
Input: A = [0,1,0,0,0,0,0,0], K = 3
i = 0, A[i] = 0, flip, A = [1,0,1,0,0,0,0,0].
i = 1, A[i] = 0, flip, A = [1,1,0,1,0,0,0,0].
i = 2, A[i] = 0, flip, A = [1,1,1,0,1,0,0,0].
i = 3, A[i] = 0, flip, A = [1,1,1,1,0,1,0,0].
i = 4, A[i] = 0, flip, A = [1,1,1,1,1,0,1,0].
i = 5, A[i] = 0, flip, A = [1,1,1,1,1,1,0,1].
output: -1
```
As shown above, the time complexity is O(NK) in the worst case.

---
3.2 Optimized solution

---

In Section 3.1, there are too many flip operations in the trivial solution.

As proved in Section 2.3, since the indexes are processed in ascending order, 

>#### **the final value of A[i]** is **ONLY determined by the parity of flip count on A[i]**.

To optimize the solution, 
a queue is used to save the biggest index of the flipped contiguous subarray.

The queue\'s size is the flip count of A[i].

---

The algorithm is optimized to a one-pass solution.
**Initially, the total flip count c equals to 0. The queue Q is empty.**
- **Loop:** iterate index i from **0 to N - 1**.
   - If **Q\'s size** is **even**, **change A[i] (0 to 1, 1 to 0)**.
   - Else, **DON\'T change A[i]**.
   - If **A[i] = 0, put i + K - 1 to Q**. **Set c = c + 1**.
   - Else, ignore.
   - If **Q is NOT empty and A[i] = the front element in Q**, **pop from Q**.
- **After processing**,
  - **If Q is empty, return c**.
  - **Else, return -1**.

---
## 4. Complexity Analysis

---

#### 4.1 Time complexity

---

As shown in Section 3.2, the number of iteration is **N**.

>#### The time complexity is **O(N)**.

---

#### 4.2 Space complexity

---

A queue is used to save the indexes, 

>#### The space complexity is **O(N)**.

---
## 5. Code

---
```
class Solution {
public:
    int minKBitFlips(vector<int>& A, int K) {
        int ans = 0;
        int size = A.size();
        queue<int> record;
        for(int i = 0; i < size; i++)
        {
            int pivot = record.size() % 2 == 0 ? A[i] : 1 - A[i];
            if(pivot == 0)
            {
                ans++;
                record.push(i + K - 1);
            }
            if(!record.empty() && i == record.front()) record.pop();
        }
        return record.empty() ? ans : -1;
    }
};
