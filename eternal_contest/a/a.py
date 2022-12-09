def read_input():
    n = input()
    tanks = [int(x) for x in input().strip().split()]
    return n, tanks


def main():
    n, tanks = read_input()
    if sorted(tanks) == tanks:
        print(tanks[-1] - tanks[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()

"""
Ввод
2
1 2

Вывод
1

Ввод
5
1 1 5 5 5

Вывод
4

Ввод
3
3 2 1

Вывод
-1

"""
