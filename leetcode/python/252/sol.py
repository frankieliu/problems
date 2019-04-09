
My Python Solution

https://leetcode.com/problems/meeting-rooms/discuss/67812

* Lang:    python3
* Author:  yinfeng.zhang.9
* Votes:   21

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
            
        return True
