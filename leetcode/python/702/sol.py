
python binary search solution

https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/discuss/238358

* Lang:    python3
* Author:  clu9
* Votes:   0

\'\'\'

        start, end = 0, 1
        while (reader.get(end) < target):
            end = end << 1
        
        while start + 1< end:
            mid = (start + end) // 2
            
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) == target:
                return mid
            else:
                end = mid
        
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
\'\'\'

The hardes is how to define \'end\'. 
I assumed end is 1 and compare target and reader.get(1) to confirm if this \'end\' is suitable.
If not use end = end << 1 to time \'end\'.
