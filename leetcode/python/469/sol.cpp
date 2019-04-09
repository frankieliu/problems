
Simple C++ Code.

https://leetcode.com/problems/convex-polygon/discuss/95572

* Lang:    cpp
* Author:  fentoyal
* Votes:   0

```
struct MyPoint
{
    int x, y;
    MyPoint operator-(MyPoint to_minus)
    {
        return MyPoint{x - to_minus.x, y - to_minus.y};
    }
    int operator*(MyPoint to_right)
    {
        return x * to_right.y - to_right.x * y;
    }
};
class Solution {
public:
    bool isConvex(vector<vector<int>>& points) {
        if (points.size() < 3)
            return false;
        int prod = 0;
        points.push_back(points[0]);
        points.push_back(points[1]);
        for (int i = 2; i < points.size(); ++i)
        {
            MyPoint pt0 {points[i - 2][0], points[i - 2][1]};
            MyPoint pt1 {points[i - 1][0], points[i - 1][1]};
            MyPoint pt2 {points[i    ][0], points[i    ][1]};
            MyPoint vec01 = pt1 - pt0, vec02 = pt2 - pt0;
            int cur_prod = vec01 * vec02;
            if (prod == 0)
                prod = cur_prod;
            else if (cur_prod != 0 && cur_prod < 0 != prod < 0)
                return false;
        }
        return true;
    }
};
```
