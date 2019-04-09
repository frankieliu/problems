
C++ O(nlogn) Graham Scan - Handling the Co-linear Case

https://leetcode.com/problems/erect-the-fence/discuss/103317

* Lang:    cpp
* Author:  fentoyal
* Votes:   0

The tricky part is how to deal with co-linear case. That's how I did it:
1. When selecting the lowest point, if there are multiple at the same y, select the leftmost one.
2. When sorting points by polar angle with the lowest point, if there are multiple at the same angle, sort them from nearest to the farthest from the lowest point.
3. When determining whether should pop the stack, only pop if the new segment is to the right of the last segment. Don't pop if they are co-linear.
4. Then you will be all good except for the last segment that points back to the lowest point. 
Consider this case:
(0,0) (1,0) (1,2) (0, 2) (0,1);
The output would be 
(0,0) (1,0) (1,2) (0, 2)
(0,1) was popped when (0,2) was added 
This is because how I handled co-linear during the sorting part (case 2). In my way, 0,2 is tested after 0,1. If I change the way to test the farthest point (to the lowest) first, then this segment is fine but the first segment leaving the lowest point will be problematic.

To resolve this, an additional test has to be done, searching from the last point backwards to push any  points lying on the last segment to the stack until it finds the first one that is not on the segment.


```
int operator*(Point pa, Point pb) //cross product
{
    return pa.x * pb.y - pa.y * pb.x;
}
bool operator<(Point pa, Point pb)//assuming pa != pb
{
    if (pa * pb == 0)
        return pa.x*pa.x + pa.y*pa.y < pb.x*pb.x + pb.y*pb.y;
   return pa * pb > 0;
}
Point operator-(Point pa, Point pb)
{
    return Point{pa.x - pb.x, pa.y - pb.y};
}
Point operator+(Point pa, Point pb)
{
    return Point{pa.x + pb.x, pa.y + pb.y};
}
class Solution {
public:
    vector<Point> outerTrees(vector<Point>& points) {
        if (points.size() <= 3)
            return points;
        auto miniter = min_element(points.begin(), points.end(), [](Point a, Point b){return a.y < b.y || (a.y == b.y && a.x < b.x);});
        Point low_pt = *miniter;
        swap(*miniter, *points.begin());
        transform(points.begin(), points.end(), points.begin(), [low_pt](Point p){return p - low_pt;});
        sort(points.begin() + 1, points.end());
        vector<Point> pt_stack {points[0], points[1], points[2]};
        for (int i = 3; i < points.size();)
        {
            auto last = pt_stack.back(), second_last = pt_stack[pt_stack.size() - 2];
            Point base = last - second_last, test = points[i] - second_last;
            if (test * base > 0) // test if the new segment is to the right of last one
                pt_stack.pop_back();
            else
                pt_stack.push_back(points[i ++]);
        }
        for (int i = points.size() - 2; i >= 0 && points[i] * points.back() == 0; -- i)
                pt_stack.push_back(points[i]);
        transform(pt_stack.begin(), pt_stack.end(), pt_stack.begin(), [low_pt](Point p){return p + low_pt;});
        return pt_stack;
    }
};
```
