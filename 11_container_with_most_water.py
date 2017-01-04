"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

"""
Q:
    what to return exactly? The larger height of the container? Or the index of that?
    does the two lines need to be adjacent?

    Should be: return the capacity.

Note 2: no need adjacent lines.
    (1) find two lines at arbitrary positions i, j (i < j) such that (a[i], a[j]) container contains the largest amount of water
    (2) brutal-force algorithm, O(n^2)
    (3) for each a[i] (i = 0, ..., n-1), find a[j] such that a[j] is the closest value of a[i]. This would be the largest container can be formed with a[i]. (Wrong, we need also consider the distance at x-axis)
    (4) Should be: for each a[i] (i = 0, ..., n-1), find a[j] such that min(a[i], a[j]) * (j-i) is the largest. This would be the largest container can be formed with a[i].

O(n) algorithm:
    (1) initialize: max_cap = min(a[0], a[n-1]) * (n-1) and two pointers i = 0, j = n-1
    (2) if height[i] < height[j]:
            then all capacities of containers (a[i], a[j-1), (a[i], a[j-2]), ..., (a[i], a[i+1]) are no greater than
            that of (a[i], [j]) because (i) the width is decreasing; and (ii) a[i] is the bottleneck so that the maximum height of all those containers must be no greater than a[i].
            Therefore, we don't need to compute all those capacities.
            update max_cap if needed, i++
    (3) if height[i] > height[j]:
            then all capacities of containers (a[i], a[j), (a[i+1], a[j]), ..., (a[j-1], a[j]) are no greater than
            that of (a[i], [j]) due to (i) the width is decreasing; and (ii) a[j] is the bottleneck.

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        # soln 1: brutal force. Time: O(n^2); Space: O(1). Time exceeded
        n = len(height)
        max_cap, cap = 0, 0
        for i in range(n-1):
            for j in range(i+1, n):
                cap = min(height[j], height[i]) * (j-i)
                if cap > max_cap:
                    max_cap = cap
        return max_cap
        """

        # soln 2: one pass. Time: O(n); space: O(1)
        n = len(height)
        max_cap = 0

        i, j = 0, n - 1
        while i < j:
            max_cap = max(max_cap, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_cap

