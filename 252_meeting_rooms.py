"""

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

"""

"""
Q:
    (1) is "e1 = s2" allowed? start time is equal to end time of previous meeting?


Observation:
    (1) "could attend all meetings" = there is no overlaps between any pair of intervals.
    (2) we can sort all start and end times, and then check new time interval formed by current and next times.


Algorithm: Time: O(n) + O(nlog(n)) + O(n) = O(nlog(n)); Space: O(n)
    (1) put all intervals in hash table
    (2) put all times in list, then sort
    (3) check whether new intervals in list are in hash table.

Algorithm 2: Time: O(nlog(n)), Space: O(1)
    (1) sort in-place by start time, then check end time violation
    (2) if end[i] > start[i+1], violate
    (3) Note the usage of sort(key = operator.attrgetter())

"""


from operator import attrgetter
from collections import defaultdict

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        n = len(intervals)
        times = []
        lookup = defaultdict(int)

        for i in xrange(n):
            times.extend([intervals[i].start, intervals[i].end])
            lookup[(intervals[i].start, intervals[i].end)] += 1

        times.sort()

        for j in xrange(0, 2*n, 2):
            if lookup[(times[j], times[j+1])] == 0:
                return False
        return True


    def canAttendMeetings2(self, intervals):


        intervals.sort(key = attrgetter("start"))

        for i in xrange(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True

if __name__ == "__main__":
    intervals = [Interval(0, 30), Interval(0, 30), Interval(0, 30)]
    intervals = [Interval(0, 10), Interval(11, 20), Interval(25, 30)]

    print Solution().canAttendMeetings(intervals)
    print Solution().canAttendMeetings2(intervals)