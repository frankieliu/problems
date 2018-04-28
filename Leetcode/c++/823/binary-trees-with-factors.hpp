class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& A) {

        int result = A.length(); // Root nodes only

        // Root nodes with left and right children
        sort(A.begin(), A.end());

        // Initialize
        vector<int> B;
        B.resize(A.length(),0);

        for(int i: A) {
            if (i
            // For each element calculate the number of trees
            // containing it and possible factors
            numFactoredBinaryTrees
        }

        return 0;
    }
};
