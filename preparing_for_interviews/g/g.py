import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.children = []


def get_number_of_upgoing_paths(root: Node, x: int) -> int:
    res = 0

    def _dfs(node: Node, prev_prefix_sum: int):
        nonlocal res
        prefix_sum = node.weight + prev_prefix_sum
        need = prefix_sum - x
        res += freq[need]
        freq[prefix_sum] += 1
        for child in node.children:
            _dfs(child, prefix_sum)
        freq[prefix_sum] -= 1
        if freq[prefix_sum] == 0:
            del freq[prefix_sum]

    freq = defaultdict(int)
    freq[0] += 1
    _dfs(root, 0)
    return res


def read_tree(tree_size: int) -> Node:
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root


def main():
    n, x = map(int, input().split())
    tree = read_tree(n)
    print(get_number_of_upgoing_paths(tree, x))


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
