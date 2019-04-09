
C++ Dijkstra's algorithm using two maps to greatly simplify the implementation.

https://leetcode.com/problems/the-maze-iii/discuss/97806

* Lang:    cpp
* Author:  fentoyal
* Votes:   0

I greately simplified the implementation uses a few observations:
1. To account for "lexicographically smaller" requirement, we can just store the current path as part of the weight of the weight (the other part is of course the distance), so the lexicographically smaller path will be chosen if the distances are same.
2. C++'s priority queue can't decrease key value (which is the weight of an edge here). If I use other data structures like multimap, it seems I can decrease the key value (weight) by removing the old key and inserting the new key, but in fact, I can't if there are same weights in the multimap, because I can't locate a key (weight) given a value (position). 

However, based on the observation 1, if I put the current path in the weight (map's key), this will automatically make every key unique, because a same path will never appear in the map more than once -- Easy to prove: You can only obtain a path, say, lur, by adding r at path lu, if lu was not added more than once (hence not popped more than once), so can't lur. Follow this logic, as long as I don't push the first starting path twice, I won't see another path appearing twice in a map.

So based on this observation, every weight is unique too. Then I can make another map from positions --> weight, to locate a weight given a value. The problem is solved.

3. The final small issue is I need a way to record which position has been completed, so it won't be tested again. I usually set up a "visited" map to record such info. However, based on observation 2, we got a position -> weight map. So I can just change the weight of a visited position into something different, so it can record this information. So I decided to change the weight's path(a string) to be "finished" to denote this. This saved me one more map;

```
class Solution {
    using Cost = pair<int, string>;
    using Pos = pair<int, int>;
    map<Cost, Pos> cp_map;
    map<Pos, Cost> pc_map;
    map<int, vector<Pos>> neighbor_map;
    int width, height;
    vector<vector<int>> maze;
    const string directions = "dlru";
    vector<Pos> reaches(Pos p)
    {
        int loc = p.first * width + p.second;
        auto iter = neighbor_map.find(loc);
        if (iter != neighbor_map.end())
            return iter->second;
        vector<Pos> result;
        ///down
        int i = p.first;
        for (; i < height && maze[i][p.second] == 0; ++i);
        i -= (i >= height || maze[i][p.second] == 1); // wall, minus one, hole not
        result.emplace_back(i, p.second);
        ///left
        int j = p.second;
        for (; j >= 0 && maze[p.first][j] == 0; --j);
        j += (j < 0 || maze[p.first][j] == 1);
        result.emplace_back(p.first, j);
        ///right
        j = p.second;
        for (; j < width && maze[p.first][j] == 0; ++j);
        j -= (j >= width || maze[p.first][j] == 1);
        result.emplace_back(p.first, j);
        ///up
        i = p.first;
        for (; i >= 0 && maze[i][p.second] == 0; --i);
        i += (i < 0 || maze[i][p.second] == 1);
        result.emplace_back(i, p.second);

        neighbor_map[loc] = result;
        return result;
    }
    inline int distance(Pos p0, Pos p1)
    {
        return abs(p0.first - p1.first) + abs(p0.second - p1.second);
    }
public:
    string findShortestWay(vector<vector<int>>& _maze, vector<int>& ball, vector<int>& hole)
    {
        maze = std::move(_maze);
        height = maze.size();
        if (height == 0)
            return "impossible";
        width = maze.back().size();
        Cost orig_c = Cost(0, "");
        Pos orig_p = Pos(ball[0], ball[1]);
        Pos target_p = Pos(hole[0], hole[1]);
        maze[target_p.first][target_p.second] = -1;
        cp_map[orig_c] = orig_p;
        pc_map[orig_p] = orig_c;
        while(cp_map.size())
        {
            Cost cur_c = cp_map.begin()->first;
            Pos cur_p = cp_map.begin()->second;
            cp_map.erase(cur_c);
            pc_map[cur_p].second = "finished";
            if (cur_p == target_p)
                return cur_c.second;
            auto neighbors = reaches(cur_p);
            for (int i = 0; i < 4; ++i)
            {
                Pos nb_p = neighbors[i];
                char direction = directions[i];
                int dist = distance(cur_p, nb_p) + cur_c.first;
                string path = cur_c.second + direction;
                Cost nb_c = Cost(dist, path);
                auto respair = pc_map.emplace(nb_p, nb_c);
                if (!respair.second) // exist
                {
                    Cost nb_old_c = respair.first->second;
                    if (nb_old_c.second == "finished")
                        continue;
                    if (nb_c < nb_old_c)
                    {
                        cp_map.erase(nb_old_c);
                        cp_map[nb_c] = nb_p;
                        respair.first->second = nb_c;
                    }
                }else
                    cp_map[nb_c] = nb_p;
            }
        }
        return "impossible";
    }
};
```
