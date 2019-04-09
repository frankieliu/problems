
Share my O(n) C++ accumulation-modulo solution with thinking process and explanation

https://leetcode.com/problems/continuous-subarray-sum/discuss/99545

* Lang:    cpp
* Author:  KJer
* Votes:   34

---
## 1. Problem

---
Given a list of **non-negative** numbers and a target **integer** k, write a function to check if the array has a continuous subarray of size **at least 2** that sums up to the multiple of **k**, that is, sums up to n*k where n is also an **integer**

---
## 2. Thinking process

---
#### 2.1 Calculate the summation of a continuous subarray

---
As we know **the summation of series**

>#### **S(n) = a(1) + a(2) + ... + a(n), n \u2265 1**

which has a **recursion formula**

>#### **S(n) = a(1), n = 1**
>#### **S(n) = a(n) + S(n - 1), n > 1**

Suppose **the summation** of a **subarray** from **a(i)** to **a(j)** is

>#### **T(i, j) = a(i) + a(i + 1) + ... + a(j - 1) + a(j), 1\u2264 i < j \u2264 n.**

It can be inferred that 

>#### **T(i, j) = S(j), i = 1.**
>#### **T(i, j) = S(j) - S(i - 1), i > 1.**

---
#### 2.2 Define the multiple of k (k \u2260 0) by modulo

---
The problem is to find a continuous subarray of size **at least 2** that sums up to the multiple of **k**, which means

>#### **T(i, j) = n \xd7 k, 1\u2264 i < j \u2264 n.**

That is to say

>#### **S(j) = n \xd7 k , 1 = i < j.**
>#### **S(j) - S(i - 1) = n \xd7 k, 1 < i < j.**

By doing the modulo, we get

>#### **S(j) \u2261 0 mod k , 1 = i < j.**
>#### **S(j) \u2261 S(i - 1) mod k, 1 < i < j.**

---
## 3. Algorithm

---
#### 3.1. Special cases

---
**A. The size of array < 2**

- Since the size of subarray is **at least 2**, **return false**.

---
**B. k = 0**

>#### **T(i, j) = a(i) + a(i + 1) + ... + a(j - 1) + a(j) = 0.**

As the array only contains **non-negative** numbers, that is to say

>#### **a(i) = a(i + 1) = ... = a(j - 1) = a(j) = 0.**

Since the size of subarray is **at least 2**, 

- if there are **2 adjacent zeros** in the array, **return true.**

- **If not, return false.**

---
#### 3.2 Normal situation
---
**Step 1:  Summation**

---

Do iteration by using the recursion formula

>#### **S(n) = a(1), n = 1**
>#### **S(n) = a(n) + S(n - 1), n > 1.**

---
**Step 2: Modulo operation**

---
There are **2 situations**:

>#### **S(j) \u2261 0 mod k , 1 = i < j.**

>#### **S(j) \u2261 S(i - 1) mod k, 1 < i < j.**

When **doing iteration from j = 1 to j = n**, we need to judge

**A. When j > 1 and S(j) \u2261 0 mod k, return true.**

**B. Use a hash table (the key is S(i) mod k) to record THE FIRST i. If a same key appears twice (means S(j) \u2261 S(i) mod k) and j - i > 1, return true.**

(At first I didn't notice that the size is **at least 2**, thanks to @BavariaKing1822 )

**C. After the iteration, return false.**

---
## 4. Complexity analysis

---
#### 4.1 Time complexity

---
As **Step 1 and Step 2** in **Section 3** can be merged to **a single iteration from j = 1 to j = n**.

> #### **The time complexity is O(n)**.

---
#### 4.2 Space complexity

---
As the **hash table's key** is **a remainder from division based on integer k**, the **probable maximum size** of the hash table is **|k|**.

>#### **The space complexity is O(|k|)**.

---
## 5. Code

---
```
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if(nums.size() < 2) return false;
        if(k == 0)
        {
            for(int i = 1; i < nums.size(); i++)
            {
                if(nums[i] == 0 && nums[i - 1] == 0) return true;
            }
            return false;
        }else{
            int i = 0;
            map<int, int> res;
            while(true)
            {
                if(i != 0 && nums[i] % k == 0)
                {
                    return true;
                }else{
                    if(res.find(nums[i] % k) == res.end())
                    { 
                         res[nums[i] % k] = i;
                    }else{
                         if(i - res[nums[i] % k] > 1) return true;
                    }
                }
                i++;
                if(i == nums.size()) return false;
                nums[i] += nums[i - 1];
            }
        }
    }
};
```
---
