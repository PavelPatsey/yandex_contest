import sys
from typing import List, Tuple

sys.setrecursionlimit(10**7)

DIRS = ((0, 1), (-1, 0), (0, -1), (1, 0))


def in_bound(node, len_rows, len_cols):
    row, col = node
    return 0 <= row < len_rows and 0 <= col < len_cols


def get_path_length(
    n: Tuple[int, int], matrix: List[List[int]], dp: List[List[int]]
) -> int:
    def _dfs(node: Tuple[int, int]) -> int:
        r, c = node
        if dp[r][c] != 0:
            return dp[r][c]
        max_length = 1
        for dr, dc in DIRS:
            nr, nc = new_node = r + dr, c + dc
            is_suitable_neighbor = (
                in_bound(new_node, len(matrix), len(matrix[0]))
                and matrix[nr][nc] > matrix[r][c]
            )
            if is_suitable_neighbor:
                length = 1 + _dfs(new_node)
                max_length = max(max_length, length)
        dp[r][c] = max_length
        return max_length

    len_path = _dfs(n)
    return len_path


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    dp = [[0 for _ in range(len_cols)] for _ in range(len_rows)]
    res = 0
    for row in range(len_rows):
        for col in range(len_cols):
            node = row, col
            longest = get_path_length(node, matrix, dp)
            res = max(res, longest)
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
    test()
    main()

"""
input
2 3
10 8 5
10 5 4
output
4
"""
