
Python Solution (Single passthrough)

https://leetcode.com/problems/number-of-corner-rectangles/discuss/110211

* Lang:    python3
* Author:  shirtandtieler
* Votes:   0

I'm pretty pleased with this solution, simply because I was able to simplify the number-of-combinations formula (see below the code), which drastically reduced my run-time.

```
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dictionary to keep track of the indicies of '1's per each row
        y_dict = dict()
        
        # the total number of rectangles
        total = 0
        for y,row in enumerate(grid):
            
            # get all of the indices of '1's in the current row
            x_indices_curr_row = [x for x in range(len(row)) if row[x]]
            
            # then go through the previous rows, checking for any intersecting indices
            for prev_y in range(y):
                
                # ignore the rows that had none or less than 2 '1's in its row
                # (since you'd need 2 to make a single rectangle)
                if prev_y not in y_dict or len(y_dict[prev_y]) < 2:
                    continue
                
                x_indices_prev_row = y_dict[prev_y]
                
                # transform into sets in order to use the intersection function
                num_intersections = len(set(x_indices_curr_row).intersection(set(x_indices_prev_row)))
                
                # if there's at least 2 similarities, add the total number of combinations
                # (using a simplified version of the combinations formula -- see note below)
                if num_intersections >= 2:
                    total += int(0.5*num_intersections*(num_intersections-1))
                    
            # and add the current row to the dictionary
            y_dict[y] = x_indices_curr_row
            
        return total
```

As for the number-of-combinations formula, it's typically:

```
     n!
----------
r! * (n-r)!
```
Where 'n' is the number of total items, 'r' is the items you're choosing from, and the '!' is factorial (i.e. x * x-1 * x-2 * ... * 1)
But since the 'r' (and also 'r!', since 'r!' = 2 * 1 = 2) is a constant, the formula can be simplified to:
```
      n!          n * (n-1)
----------- == ----------- ==    0.5 * n * (n-1)
2 * (n-2)!           2
```
