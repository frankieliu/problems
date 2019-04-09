
My Python Solution With Explanation

https://leetcode.com/problems/meeting-rooms-ii/discuss/67860

* Lang:    python3
* Author:  yinfeng.zhang.9
* Votes:   114

     # Very similar with what we do in real life. Whenever you want to start a meeting,
     # you go and check if any empty room available (available > 0) and
     # if so take one of them ( available -=1 ). Otherwise,
     # you need to find a new room someplace else ( numRooms += 1 ).
     # After you finish the meeting, the room becomes available again ( available += 1 ).

     def minMeetingRooms(self, intervals):
            starts = []
            ends = []
            for i in intervals:
                starts.append(i.start)
                ends.append(i.end)

            starts.sort()
            ends.sort()
            s = e = 0
            numRooms = available = 0
            while s < len(starts):
                if starts[s] < ends[e]:
                    if available == 0:
                        numRooms += 1
                    else:
                        available -= 1

                    s += 1
                else:
                    available += 1
                    e += 1

            return numRooms
