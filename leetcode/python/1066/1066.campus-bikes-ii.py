#
# @lc app=leetcode id=1066 lang=python
#
# [1066] Campus Bikes II
#
# https://leetcode.com/problems/campus-bikes-ii/description/
#
# algorithms
# Medium (43.65%)
# Total Accepted:    1.8K
# Total Submissions: 4K
# Testcase Example:  '[[0,0],[2,1]]\n[[1,2],[3,3]]'
#
# On a campus represented as a 2D grid, there are N workers and M bikes, with N
# <= M. Each worker and bike is a 2D coordinate on this grid.
#
# We assign one unique bike to each worker so that the sum of the Manhattan
# distances between each worker and their assigned bike is minimized.
#
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) =
# |p1.x - p2.x| + |p1.y - p2.y|.
#
# Return the minimum possible sum of Manhattan distances between each worker
# and their assigned bike.
#
#
#
# Example 1:
#
#
#
#
# Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# Output: 6
# Explanation:
# We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of
# both assignments is 3, so the output is 6.
#
#
# Example 2:
#
#
#
#
# Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# Output: 4
# Explanation:
# We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker
# 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the
# Manhattan distances as 4.
#
#
#
#
# Note:
#
#
# 0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
# All worker and bike locations are distinct.
# 1 <= workers.length <= bikes.length <= 10
#
#
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)
        # 0 ~ m - 1  workers
        # m ~ m + n - 1 bikes
        s = m + n # dummy source
        t = s + 1 # dummy sink
        num_nodes = m + n + 2
        g =[[] for _ in range(num_nodes)]
        prevv = [None] * num_nodes
        preve = [None] * num_nodes

        def add_edge(from_node, to_node, cap, cost):
            g[from_node].append([to_node, cap, cost, len(g[to_node])])
            # reverse edge
            g[to_node].append([from_node, 0, -cost, len(g[from_node]) - 1])

        # find minimum cost to flow f from s to t
        def min_cost_flow(s, t, f):
            res = 0
            # Bellman-Ford
            while f > 0:
                dist = [float('inf')] * (m + n + 2)
                dist[s] = 0
                update = True
                while update:
                    update = False
                    for v in range(num_nodes):
                        if dist[v] == float('inf'):
                            continue
                        for i in range(len(g[v])):
                            edge = g[v][i]
                            # if there is capacity left on this edge and
                            # it costs less to go to the next node from here
                            if edge[1] > 0 and dist[edge[0]] > dist[v] + edge[2]:
                                dist[edge[0]] = dist[v] + edge[2]
                                prevv[edge[0]] = v
                                preve[edge[0]] = i
                                update = True
                assert dist[t] != float('inf')
                d = f
                v = t
                count_edges = 0
                while v != s:
                    d = min(d, g[prevv[v]][preve[v]][1])
                    v = prevv[v]
                    print("count {} edge {}".format(count_edges,v))
                    count_edges += 1
                print(g)
                print("min cap {}, num_edges {}".format(d, count_edges))
                f -= d
                res += d * dist[t]
                v = t
                while v != s:
                    edge = g[prevv[v]][preve[v]]
                    edge[1] -= d
                    g[v][edge[3]][1] += d
                    v = prevv[v]
            return res

        for i in range(m):
            for j in range(n):
                x1, y1 = workers[i]
                x2, y2 = bikes[j]
                c = abs(x1 - x2) + abs(y1 - y2)
                add_edge(i, m + j, 1, c)
        for i in range(m):
            add_edge(s, i, 1, 0)
        for i in range(n):
            add_edge(m + i, t, 1, 0)

        return min_cost_flow(s, t, m)

test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*2
    if case[0]:
        # Example 1:
        workers = [[0,0],[2,1]]
        bikes = [[1,2],[3,3]]
        # Output: 6
        print(sol.assignBikes(workers, bikes))
    if case[1]:
        # Example 2:
        workers = [[0,0],[1,1],[2,0]]
        bikes = [[1,0],[2,2],[2,1]]
        # Output: 4
        print(sol.assignBikes(workers, bikes))

