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

        // accumulate individual results
        int out = 0;

        // Sort so as to compute intermediate results
        //  that is root at position n will depended on
        //  results from position [0,n-1]
        //
        //  If we begin with the smallest element and
        //  work our way up, then we don't need to
        //  recurse on the smaller solutions.
        sort(A.begin(), A.end());
        
        // save intermediate results
        map<int,int> saved;
        for (auto i: A) saved[i] = 0;

        int ind = 0; // current position in A
        for(int root: A) { // consider trees with root node "root"

            // The self result (single root node)
            int result = 1;

            // Trees with children factors:

            // Possible factors
            set<int> factors(A.begin(),
                             A.begin()+ind+1);

            for (int f: factors) {
                // Find the other factor
                int a = (int) (root / f);
                if ((root == a*f) && (factors.count(a) >= 1)) {
                    factors.erase(a);
                    int tmp = saved[f];

                    // Check if both factors are the same
                    if (a != f) {
                        result += 2*tmp*saved[a];
                    } else {
                        result += tmp;
                    }
                }
            }
            saved[root] = result;
            // cout << root << " " << saved[root] << endl;
            ind++;
            out += saved[root];
        }
        return out;
    }
};
