from collections import defaultdict


def read_input():
    n = int(input())
    orders = []
    for _ in range(n):
        line = input().strip().split()
        dt = int(line[1]) - int(line[0])
        orders.append([int(line[0]), int(line[1]), int(line[2]), dt])

    m = int(input())
    requests = []
    for _ in range(m):
        requests.append(input().strip().split())
    requests = [[int(y) for y in x] for x in requests]

    return n, orders, m, requests


def main():
    n, orders, m, requests = read_input()


if __name__ == "__main__":
    main()

"""
1
10 100 1000
6
1 10 1
1 10 2
10 100 1
10 100 2
100 1000 1
100 1000 2

Вывод
1000 0 1000 90 0 90 
"""
