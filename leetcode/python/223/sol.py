
Python concise solution.

https://leetcode.com/problems/rectangle-area/discuss/62139

* Lang:    python3
* Author:  caikehe
* Votes:   50

        
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap
