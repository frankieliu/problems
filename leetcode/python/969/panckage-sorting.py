"""969. Pancake Sorting
Virtual User Accepted: 0
Virtual User Tried: 0
Virtual Total Accepted: 0
Virtual Total Submissions: 0

Difficulty: Medium

Given an array A, we can perform a pancake flip: We choose some
positive integer k <= A.length, then reverse the order of the first k
elements of A.  We want to perform zero or more pancake flips (doing
them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that
sort A.  Any valid answer that sorts the array within 10 * A.length
flips will be judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:

We perform 4 pancake flips, with k values 4, 2, 4, and 3.

Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []

Explanation: The input is already sorted, so there is no need to flip anything.

Note that other answers, such as [3, 3], would also be accepted.

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""


class Solution:
    def flip(a, k):
        for el in a:
            if el[1] <= k:
                el[1] = k - el[1]

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = [x-1 for x in A]
        a = [list(reversed(x)) for x in enumerate(A)]
        a = sorted(a)

        out = []

        # position in sorted array
        j = len(A) - 1
        # find element at unsorted j
        elj = A[j]

        while j > 0:
            if a[j][1] == j:  # already at correct position
                j -= 1
                elj = A[j]
                continue

            # do first flip to end in 0th position
            if a[j][1] == 0:  # don't flip
                pass
            else:
                out.append(a[j][1]+1)

            # do second flip to move to jth position
            out.append(j+1)

            # update all positions
            print("elj", elj)
            for i in range(0, j):
                print("In loop i", i, elj)
                if i == elj:
                    print("Assign elj to 0", elj)
                    a[elj][1] = 0
                else:
                    a[i][1] = a[i][1] + 1
                    if a[i][1] == j-1:
                        new_elj = i
            elj = new_elj
            print("elj", elj)
            print(a)
            j -= 1

        return out


from itertools import permutations
ll = list(permutations(range(1, 5)))

s = Solution()
for al in ll:
    print(al)
    print(s.pancakeSort(al))
