class Solution {
public:

    // Find the number of trees with a particular root
    // factors contains the other potential children of
    // root
    int treesWithRoot(int root, set<int>& factors) {

        // There will always be one root (itself)
        int result = 1;
        for (int f: factors) {
            int a = (int) (root / f);
            if ((root == a*f) && (factors.count(a) >= 1)) {
                factors.erase(a);
                int tmp = treesWithRoot(f, factors);
                if (a != f) {
                    result += 2*tmp*treesWithRoot(a, factors);
                } else {
                    result += tmp;
                }
            }
        }
        return result;
        
    }
    
    int numFactoredBinaryTrees(vector<int>& A) {

        // Root nodes with left and right children
        sort(A.begin(), A.end());

        // Intermediate results
        vector<int> scan(0, A.size());

        // If we begin with the smallest element and
        // work our way up, then we don't need to
        // recurse on the smaller solutions.

        // Consider root nodes i
        int ind = 0; // current index into A
        for(int i: A) { 
            int result = 1; // you always have the self result
            set<int> factors(A.begin(),A ind)= 
            for (int f: factors) {
            int a = (int) (root / f);
            if ((root == a*f) && (factors.count(a) >= 1)) {
                factors.erase(a);
                int tmp = treesWithRoot(f, factors);
                if (a != f) {
                    result += 2*tmp*treesWithRoot(a, factors);
                } else {
                    result += tmp;
                }
            }
        }
        return result;

        set<int> s(A.begin(),A.end());


        cout << treesWithRoot(A[0], s) << endl;
    }
    
};
