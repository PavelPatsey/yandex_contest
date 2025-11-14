import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10**7)


def get_number_of_upgoing_paths(
    graph: List[List[int]], weight: List[int], root: int, x: int
) -> int:
    res = 0

    def _dfs(i: int, pi: int):
        nonlocal res
        if pi == -1:
            prefix_sum = weight[i]
        else:
            prefix_sum = weight[i] + prefix_sums[pi]
        prefix_sums[i] = prefix_sum
        need = prefix_sum - x
        res += freq[need]
        freq[prefix_sum] += 1
        for j in graph[i]:
            _dfs(j, i)
        freq[prefix_sum] -= 1
        if freq[prefix_sum] == 0:
            del freq[prefix_sum]

    prefix_sums = [0] * len(graph)
    freq = defaultdict(int)
    freq[0] += 1
    _dfs(root, -1)
    return res


def read_tree(n):
    parent = [-1] * n
    weight = [0] * n
    graph = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        p, w = map(int, input().split())
        parent[i] = p
        weight[i] = w
        if p == -1:
            root = i
    for i in range(n):
        if parent[i] != -1:
            graph[parent[i]].append(i)
    return root, graph, weight


def main():
    n, x = map(int, input().split())
    root, graph, weight = read_tree(n)
    print(get_number_of_upgoing_paths(graph, weight, root, x))


if __name__ == "__main__":
    main()


"""
input
6 3
-1 1
0 1
0 1
1 1
2 2
3 1
output
3


input
1 2
-1 1
output
0

input
5 0
-1 0
0 0
1 0
2 0
3 0
output
15

input
3 0
-1 -1
0 2
1 -1
output
1

input
3 2
-1 1
0 2
0 2
output
2
"""
