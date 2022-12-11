def read_input():
    n = int(input())
    orders = [[int(y) for y in x] for x in (input().strip().split() for _ in range(n))]

    m = int(input())
    requests = [
        [int(y) for y in x] for x in (input().strip().split() for _ in range(m))
    ]

    return n, orders, m, requests


def get_response(order, request):
    type = request[2]
    if type == 1 and request[0] <= order[0] <= request[1]:
        return order[2]
    elif type == 2 and request[0] <= order[1] <= request[1]:
        return order[1] - order[0]

    return 0


def main():
    n, orders, m, requests = read_input()

    responses = []
    for request in requests:
        storage = 0
        for order in orders:
            storage += get_response(order, request)
        responses.append(storage)

    print(" ".join(str(n) for n in responses))


if __name__ == "__main__":
    # assert get_response([10, 100, 1000], [1, 10, 1]) == 1000
    # assert get_response([10, 100, 1000], [1, 10, 2]) == 0
    # assert get_response([10, 100, 1000], [10, 100, 1]) == 1000
    # assert get_response([10, 100, 1000], [10, 100, 2]) == 90
    # assert get_response([10, 100, 1000], [100, 1000, 1]) == 0
    # assert get_response([10, 100, 1000], [100, 1000, 2]) == 90
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
