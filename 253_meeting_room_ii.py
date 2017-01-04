"""

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.


"""
"""

Algorithm: Time: O(nlog(n)); space: O(n)
    (1) use min-heap to maintain the smallest end time
    (2) each time when checking with an interval, if its start time is no larger than minimum end time in heap, we can then append that interval to the meeting room occupied by the interval associated with the minimum time in heap. Thus we modify the end time of that room. If not, we have to open a new room.

"""

from heapq import heappush, heappop
import operator

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=operator.attrgetter('start'))
        res = []
        heappush(res, (intervals[0].end, intervals[0].start))

        for i in range(1, len(intervals), 1):
            end, start = heappop(res)
            if intervals[i].start >= end:
                end = intervals[i].end
            else:
                heappush(res, (intervals[i].end, intervals[i].start))

            heappush(res, (end, start))

        return len(res)

if __name__ == "__main__":
    intervals = [Interval(2, 15), Interval(36, 45), Interval(9, 29), \
                 Interval(16, 23), Interval(4, 9)]


    print Solution().minMeetingRooms(intervals)



