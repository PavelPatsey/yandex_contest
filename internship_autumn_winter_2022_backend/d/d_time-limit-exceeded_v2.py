from functools import reduce


def read_input():
    n = int(input())
    orders = [[int(y) for y in x] for x in (input().strip().split() for _ in range(n))]

    m = int(input())
    requests = [
        [int(y) for y in x] for x in (input().strip().split() for _ in range(m))
    ]

    return n, orders, m, requests


def main():
    n, orders, m, requests = read_input()

    responses = []
    for request in requests:
        type = request[2]
        if type == 1:
            filtered = filter(lambda x: request[0] <= x[0] <= request[1], orders)
            res = reduce(lambda acc, x: acc + x[2], filtered, 0)
        elif type == 2:
            filtered = filter(lambda x: request[0] <= x[1] <= request[1], orders)
            res = reduce(lambda acc, x: acc + x[1] - x[0], filtered, 0)
        responses.append(res)

    print(" ".join(str(n) for n in responses))


if __name__ == "__main__":
    main()

"""
Ввод
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

Ввод
5
5 20 5
6 21 4
6 22 3
7 23 2
10 24 1
3
6 11 1
4 6 1
7 11 1

Вывод
10 12 3 
"""
