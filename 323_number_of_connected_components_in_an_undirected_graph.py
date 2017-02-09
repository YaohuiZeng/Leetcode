"""

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to
find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]
 and thus will not appear together in edges.

"""

from collections import defaultdict

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        new_edges = defaultdict(list)
        for e in edges:
            new_edges[e[0]].append(e[1])
            new_edges[e[1]].append(e[0])

        visited, stack, ncomp = set(), [], 0
        for v in xrange(n):
            if v not in visited:
                ncomp += 1
                visited.add(v)
                stack.extend([x for x in new_edges[v] if x not in visited])

                while stack:
                    cur_node = stack.pop()
                    if cur_node not in visited:
                        visited.add(cur_node)
                        stack.extend([x for x in new_edges[cur_node] if x not in visited])

        return ncomp
