class Solution {
public:

    int min(vector<int>& A) {
        int min = A[0];
        for(int i = 0; i < A.size(); i++){
            if (A[i] < min) {
                min = A[i];
            }
        }
        return min;
    }

    int min(int a, int b){
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }

    vector<vector<int>> subarray(vector<int>& A) {
        for (auto a: A) {
            // a.push_back(A[0]);
        }
        if (A.size() == 0) {
        }
        return vector<vector<int>>();
    }

    // Let's work on the subproblem
    vector<int> leftArray(vector<int>& v) {
        // Finds the left most boundary region for which boundary point > v[i]
        // For example:
        // v = [3 1 2 4]
        // l = [0 1 2 3]
    }

    // Let's make sure that this is the same result as in
    // https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution
    // EXPECT_EQ(vector<int>({1,2,1,1}),
    //   s.leetLeft(vector<int>({3,1,2,4})));
    //                           0 1 0 0
    //                          {3 2 1 0}
    //                           0 1 2 3
    //
    // Here it is cummulative: if you add the one to your left, then you
    // accummulate left[i-1] as well
    //
    // So why do you need a stack?
    //
    // For every i, you push
    // push (A[i], count)
    //
    // Then for i+1, if the stack is empty then you go ahead and push
    //  (A[i], 1)
    //
    // Otherwise, if there is something in the stack,
    // check to see if top of the stack is greater, if it is,
    // then add count += count[i-1]
    //

    vector<int> leetLeft(vector<int> A) {
        int n = A.size();
        vector<int> left(n);
        stack<pair<int, int>> s1;
        for (int i = 0; i < n; ++i) {
            int count = 1;
            while (!s1.empty() && s1.top().first > A[i]) {
                count += s1.top().second;
                s1.pop();
            }
            s1.push({A[i], count});
            left[i] = count;
        }
        for (int e : left) {
            cout << e << " ";
        }
        cout << endl;
        return left;
    }

    vector<int> leetRight(vector<int> A) {
        int n = A.size();
        vector<int> right(n);
        stack<pair<int, int>> s2;
        for (int i = n - 1; i >= 0; --i) {
            int count = 1;
            while (!s2.empty() && s2.top().first >= A[i]) {
                count += s2.top().second;
                s2.pop();
            }
            s2.push({A[i], count});
            right[i] = count;
        }
        for (int e : right) {
            cout << e << " ";
        }
        cout << endl;
        return right;
    }

    int leetSumSubarrayMins(vector<int>& A) {
        if (A.size() == 0) {
            return 0;
        } else if (A.size() == 1) {
            return A[0];
        } else {
            vector<int> left = leetLeft(A);
            vector<int> right = leetRight(A);
            int cur = 0;
            for (auto i = 0; i < A.size(); i++) {
                cur += (left[i] * right[i]) * A[i];
            }
            return cur;
        }
    }

    // This is a different decomposition of the problem
    // 0 1 2 3 4 5  <- indices of the the array
    // Subarrays are counted as:
    // ending in 0:
    // 0
    // ending in 1:
    // 0 1
    // 1
    // ending in 2:
    // 0 1 2
    // 1 2
    // 2
    // ending in 3:
    // 0 1 2 3   => note that 2 is counted here many times
    // 1 2 3
    // 2 3
    // 3
    //
    // Previous solution was counting all the subarrays containing A[i]
    
    int sumSubarrayMins(vector<int>& A){
        int MOD = 1000000007;
        int sol = 0;

        // number of subarrays containing A[i] as the last element
        // for which A[i] is a minimum
        vector<int> cur(A.size(), 0);
        stack<int> s;
        for (int i = 0; i < A.size(); ++i){

            // gets rid of previoux elements which
            // are bigger than current element
            while(!s.empty() && A[i] < A[s.top()])
                s.pop();

            cur[i] = 0;

            // if there are no elements left in the stack
            // it means that A[i] is the smallest element
            // up to the ith element
            if(s.empty()){
                // example: 5 4 3 2 1 -> stack will be empty
                // this will count all the subarrays 
                cur[i] = (i + 1)*A[i];
            } else {

                // This is the real cool calculation:
                //
                //          0 1 2 3 4
                // example: 3 3 6 5 4
                // the number of subarrays then contain
                // everything from 6 5 4
                // s.top = 1, i = 4
                //
                //                      (3  elements)*A[i] correct
                //
                //                       +
                //
                //       remaining min subarray sums! with 6 5 4 suffix!
                //
                cur[i] = cur[s.top()] + (i - s.top())*A[i];
            }
            cur[i] %= MOD;
            s.push(i);

            sol += cur[i];
            sol %= MOD;
        }
        return sol;
    }
};
 
    /*
    -inf,3,1,2,4,-inf
    i,n = 0, -inf
    s = [0]

    i,n = 1, 3
      A[0] > 3? no
      s = [0, 1]

    i,n = 2, 1
      A[stack[-1]] > A[2]
              A[1] > A[2]
                 3 > 1
                   yes
        cur = 1
        res += A[cur] * (2 - 1) * (1 - 0)
        A[3] is a peak therefore there is only
        one subarray containing 3 as the max

      A[stack[-1]] > A[2]
              A[0] > A[2]
              -inf > 1
                  no
       s = [0 2]
     i, n = 3, 2
       A[start[-1]] > A[3]?
               A[2] > A[3]?
                  1 > 2 ?
                    no
       s = [0, 2, 3]  => increasing stack
     i, n = 4, 4
       s = [0, 2, 3, 4]
     i, n = 5, -inf
       A[4] > A[5]?
          4 > -inf?
            yes
       cur = 4
       res += A[4] * (5-4) * (4-3)
       A[4] is a peak
       A[3] > A[5]?
           yes
       cur = 3
       res += A[3] * (5-3) * (3-2)
           += A[3] * 2
       A[2] > A[5]? yes
       cur = 2
       res += A[2] * (5-2) * (2-0)
       A[0] > A[5]? no

      end of enumerate

    */
