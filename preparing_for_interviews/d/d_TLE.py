from typing import List, Set, Tuple

DIRS = ((0, 1), (-1, 0), (0, -1), (1, 0))


def in_bound(node, len_rows, len_cols):
    row, col = node
    return 0 <= row < len_rows and 0 <= col < len_cols


def get_path_length(
    node: Tuple[int, int],
    matrix: List[List[int]],
    visited: Set,
    prev_value: int,
) -> int:
    if node in visited:
        return len(visited)
    if not in_bound(node, len(matrix), len(matrix[0])):
        return len(visited)
    row, col = node
    if matrix[row][col] <= prev_value:
        return len(visited)
    lengths = []
    for dr, dc in DIRS:
        new_node = row + dr, col + dc
        lengths.append(
            get_path_length(new_node, matrix, visited | {node}, matrix[row][col])
        )
    return max(lengths)


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    res = 0
    for row in range(len_rows):
        for col in range(len_cols):
            node = row, col
            length = get_path_length(
                node=node, matrix=matrix, visited=set(), prev_value=-1
            )
            res = max(res, length)
    return res


def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


def main():
    matrix = read_matrix()
    print(get_longest_increasing_path(matrix))


def test():
    assert get_longest_increasing_path([[10, 8, 5], [10, 5, 4]]) == 4
    assert get_longest_increasing_path([[1, 1], [1, 1]]) == 1
    assert get_longest_increasing_path([[10, 9], [9, 11]]) == 2


if __name__ == "__main__":
    # test()
    main()

"""
input
2 3
10 8 5
10 5 4
output
4
"""
