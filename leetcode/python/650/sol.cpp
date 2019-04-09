
Share my 3ms C++ math solution with proof and explanation

https://leetcode.com/problems/2-keys-keyboard/discuss/105944

* Lang:    cpp
* Author:  KJer
* Votes:   0

---
## 1. Problem

---
 Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    1. Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    2. Paste: You can paste the characters which are copied last time.

Given a number n. You have to get **exactly** n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'. 

---
## 2. Thinking process

---
#### 2.1 Calculate for small n's and find the formula

---
Suppose that when the given number is n, the result is f(n).

---
For n = 1,2,3,4,5,6, we can calculate

---
>#### **f(1) = 0, Initially 'A', no COPY, no PASTE**.

>#### f(2) = 1 + 1 = 2, ***COPY 'A', PASTE 'A'***.

>#### f(3) = 1 + 1 + 1 = 3, ***COPY 'A', PASTE 'A', PASTE 'A'***.

>#### f(4) = 1 + 1 + 1 + 1 = 4, COPY 'A', PASTE 'A', **COPY 'AA', PASTE 'AA'**.

>#### f(5) = 1 + 1 + 1 + 1 + 1 = 5, ***COPY 'A', PASTE 'A', PASTE 'A', PASTE 'A', PASTE 'A'***.

>#### f(6) = 1 + 1 + 1 + 1 + 1 = 5, COPY 'A', PASTE 'A', PASTE 'A', **COPY 'AAA', PASTE 'AAA'**.

---

**What do you discover?**

>#### When we **get 'AAAA'**, we **first get 'AA'**, and then **COPY and PASTE**, 

which means

>#### **f(4) = f(2) + 2.**

----
>#### When we **get 'AAAAAA'**, we **first get 'AAA'**, and then **COPY and PASTE**.

which means

>#### **f(6) = f(3) + 2.**

----
Let's go deeper.

---
When **calculating f(4)**,

>#### First, **calculate f(2) and get 'AA'**, and make 'AA' as a **Group G**.

Then, 

>#### Since **4 can be divided by 2**, **'AAAA' becomes 'GG', and we have an initial 'G'.**

which means 

>#### **Another f(2) is required to get 'GG' from 'G' (same with getting 'AA' from an initial 'A')**.

The finally result is

>#### **f(4) = f(2) + f(2).**

Similarly,

>#### **f(6) = f(2) + f(3).**

---
For **prime numbers (like 2 and 3 in the example)**, since

>#### **Prime numbers can not be devided by any number except 1 and itself.**

The **ONLY** way to get n 'A's **when n is a prime number** is to 

>#### **COPY 'A' and do PASTE 'A' for n - 1 times**.

which means

>#### **f(n) = n, n is a prime number**.

---
#### 2.2 The basic formula

---
As mentioned in 2.1, we can infer that

- #### When **n = 1, f(n) = 0**

- #### When **n** is a **prime number**, **f(n) = n.**

- #### When **n** is a **composite number**
  - #### Take a **non-1-factor d**. Since
      - #### **f(d)** is the **minimum number of steps** to get **d 'A's** from the **initial single 'A'**.
      - #### Set **d 'A's** as an **initial group**.
      - #### **f(n/d)** is the **minimum number of steps** to get **n/d groups** from the **initial single group**.
  - #### **f(d) + f(n/d)** will be the **minimum number of steps** to get **n 'A's** from the **initial single group** with **d 'A's**.
  - #### **Iterate over all d's, the minimum sum f(n) = min[f(d) + f(n/d)] is what we need.**

---
>#### **The basic formula**

>#### ![The basic formula](/assets/uploads/files/1501489415826-basic_formula.png) 

---
Since f(n) depends on former value f(d) and f(n/d), this algorithm based on the basic formula can be implemented by dynamic programming, but **the factor iteration increases the time complexity**.

---
#### 2.3 The advanced formula

---

Before making the calculation simple,  I need to do a proof by mathematical induction based on the basic formula.

---
>#### **Proof: When n is a composite number, f(n) = sum of all n's prime factors.**

---

**Step 1**: **When n has and ONLY has 2 prime factors p and q (p = q or p \u2260 q**), then

- #### **f(n) = f(p) + f(q) = p + q.**

---
**Step 2**: **For ALL n that has and ONLY has m prime factors p1, p2, ... , pm**, we **assume that the formula**
- #### **f(n) = f(p1) + f(p2) + ... + f(pm) = p1 + p2 + ... + pm** is **workable for all m \u2264 k, k \u2265 2.**

---
**Step 3**: **When n has and ONLY has k + 1 prime factors**, we can infer
- #### n can be factorized into **2 non-1-factors R and S** (**can be prime or not prime**), which means 
   - #### n = R \xd7 S, R,S \u2260 1.
- #### R has i (1 \u2264 i < k+1) prime factors, and S has j (1 \u2264 j < k+1) prime factors, and  i + j = k + 1
- #### As **R and S has no more than k prime factors**, based on the assumption in Step 2, 
  - #### **f(R) = sum of R's prime factors.**
  - #### **f(S) = sum of S's prime factors.**
- #### **f(R) + f(S) = sum of R's prime factors + sum of S's prime factors = sum of n's prime factors.**

- #### **When do iteration over all n's non-1-factor R**, 
   - #### **f(n) = min[f(R) + f(S)] = sum of n's prime factors = constant.**

---
> #### **Q.E.D.**

---
>#### **The advanced formula**

>#### ![The advanced formula](/assets/uploads/files/1501490097310-advanced_formula.png) 
---
>#### **Notice:** When n is a prime number, f(n) = n is also included in the formula.

---
#### 2.4 Algorithm design

---
Here, [**Sieve of Eratosthenes**][1] algorithm is used to get all prime numbers from 2 to n.

The program needs a **size-n-boolean-array isPrime** to save **whether an index i(starting from 2) is a prime number or not**.

- #### **Iterate i from 2 to n, when isPrime[i] is true**, 

    - #### **Mark isPrime[2i], isPrime[3i], ... as false**.
    - #### **If n can be divided by i, divide n by i and add i to the result repeatedly until n can not be divided by i**.

- #### Return the final result.

---
## 3. For your reference

---
The sequence has already been catalogued by [**OEIS**][2] (with serial number [**A134875**][3]).

---
## 4. Code

---
```
class Solution {
public:
    int minSteps(int n) {
        if(n == 1) return 0;
        int count = 0;
        bool *isPrime = new bool[n + 1];
        for(int i = 2; i < n + 1; i++) isPrime[i] = true;
        for(int i = 2; i < n + 1; i++)
        {
            if(isPrime[i] == true)
            {
                while(n % i == 0)
                {
                    count += i;
                    n /= i;
                }
                for(int j = i * i; j < n + 1; j += i) 
                {
                    if(isPrime[j]) isPrime[j] = false;
                }
            }
        }
        return count;
    }
};
```

[1]: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
      "Wikipedia: Sieve of Eratosthenes"
[2]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
      "Wikipedia: On-Line Encyclopedia of Integer Sequences"
[3]: https://oeis.org/A134875
      "OEIS: a(n)=the smallest sum of two nontrivial divisors of n, if any, whose product equals n; otherwise, a(n)=n. "
