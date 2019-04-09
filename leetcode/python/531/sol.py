
Python - Single Pass - O(MN) time - O(M+N) space - Pruned Search Space

https://leetcode.com/problems/lonely-pixel-i/discuss/100082

* Lang:    python3
* Author:  humachine
* Votes:   0

Some ideas we use to form this solution:
- Assume we see the first 'B' in a particular row at column j1.  
If we see another 'B' in the same row at column j2, then we can be certain that no cell on this row/column j1/column j2 can ever have a lonely pixel. 
- If there was exactly one 'B' in the row, we go through column j1 from the current row and below. Any 'B's we encounter mean that there can never be a lonely pixel on the rows that we see these pixels. 

Essentially we have a set of possible rows and columns that could potentially have lonely pixels. Every time we see 'B's, we see if it's a lonely pixel (or eliminate potential rows/columns in the process).

````
    def findLonelyPixel(self, picture):
        m, n = len(picture), len(picture[0])
        lonely_pixel_count = 0
        invalid_rows, invalid_cols = [False]*m, [False]*n

        for row in xrange(m):
            # If this row has already been ininvalidated, we move on to the next row.
            if invalid_rows[row]:
                continue
            count, col = 0, None
            for j in xrange(n):
                if picture[row][j] == 'B':
                    count, col = count+1, j
                    # If we have more than one 'B' on this row, then every column that has a 'B' is ininvalid
                    if count>1:
                        invalid_cols[col] = True
                        invalid_cols[j] = True

            if count==1 and not invalid_cols[col]:
                lonely = True
                for i in xrange(row+1, m):
                    # If we see another 'B' on the rest of the column, every row with a 'B' is invalid.
                    if picture[i][col] == 'B':
                        invalid_rows[i] = True
                        lonely = False
                if lonely:
                    lonely_pixel_count+=1
                invalid_cols[col] = True
        return lonely_pixel_count

````
