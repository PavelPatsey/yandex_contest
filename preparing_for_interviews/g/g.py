class Node:
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.children = []
        self.prefix_sum = None

    def __repr__(self):
        return (
            f"w={self.weight},p={self.parent},ps={self.prefix_sum},ch={self.children}"
        )


def get_number_of_upgoing_paths(root: Node, x: int) -> int:
    # your code goes here
    return 0


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
            nodes[i].prefix_sum = nodes[i].weight + nodes[nodes[i].parent].prefix_sum
        else:
            nodes[i].prefix_sum = nodes[i].weight
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
"""
