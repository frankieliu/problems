#
# @lc app=leetcode id=1152 lang=python
#
# [1152] Analyze User Website Visit Pattern
#
# https://leetcode.com/problems/analyze-user-website-visit-pattern/description/
#
# algorithms
# Medium (37.20%)
# Total Accepted:    962
# Total Submissions: 2.5K
# Testcase Example:  '["joe","joe","joe","james","james","james","james","mary","mary","mary"]\n[1,2,3,4,5,6,7,8,9,10]\n["home","about","career","home","cart","maps","home","home","about","career"]'
#
# We are given some website visits: the user with name username[i] visited the
# website website[i] at time timestamp[i].
#
# A 3-sequence is a list of websites of length 3 sorted in ascending order by
# the time of their visits.  (The websites in a 3-sequence are not necessarily
# distinct.)
#
# Find the 3-sequence visited by the largest number of users. If there is more
# than one solution, return the lexicographically smallest such 3-sequence.
#
#
#
# Example 1:
#
#
# Input: username =
# ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
# timestamp = [1,2,3,4,5,6,7,8,9,10], website =
# ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation:
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2
# users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1
# user.
#
#
#
#
# Note:
#
#
# 3 <= N = username.length = timestamp.length = website.length <= 50
# 1 <= username[i].length <= 10
# 0 <= timestamp[i] <= 10^9
# 1 <= website[i].length <= 10
# Both username[i] and website[i] contain only lowercase characters.
# It is guaranteed that there is at least one user who visited at least 3
# websites.
# No user visits two websites at the same time.
#
#
#
from collections import defaultdict, Counter
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        trip = sorted(zip(username, timestamp, website))
        # print(list(trip))
        trip2 = defaultdict(list)
        for u,t,w in trip:
            trip2[u].append(w)
        # print(trip2)
        trip3 = []
        for k,v in trip2.items():
            trip4 = set() 
            # print(k,v)
            if len(v) < 3:
                continue
            for i in range(0, len(v)-3+1):
                for j in range(i+1, len(v)-2+1):
                    for k in range(j+1, len(v)):
                        tup = (v[i],v[j],v[k])
                        if tup in trip4:
                            continue
                        else:
                            trip4.add(tup)
                            trip3.append(tup)
        trip4 = Counter(trip3)
        maxc = 0
        maxt = None
        for k,v in trip4.items():
            # print(k,v)
            if v >= maxc:
                if maxt is None or k < maxt and v == maxc or v > maxc:
                    maxt = k
                    maxc = v
        return list(maxt)

test = True
if test:
    sol = Solution()
    case = [False]*1 + [True] + [False]*1
    if case[0]:
        # Example 1:
        # Input:
        username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
        timestamp = [1,2,3,4,5,6,7,8,9,10]
        website = ["home","about","career","home","cart","maps","home","home","about","career"]
        # Output: ["home","about","career"]
        print(sol.mostVisitedPattern(username, timestamp, website))
    if case[1]:
        username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
        timestamp = [436363475,
                     710406388,
                     386655081,
                     797150921]
        website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
        #✘ answer: ["oz","wnaaxbfhxp","mryxsjc"]
        #✘ expected_answer: ["oz","mryxsjc","wlarkzzqht"]
        print(sol.mostVisitedPattern(username, timestamp, website))
