SEATS_DICT = {0: "A", 1: "B", 2: "C", 4: "D", 5: "E", 6: "F"}


def read_input():
    n = int(input())
    seats = []
    for _ in range(n):
        seats.append(input())
    seats = [[y for y in x] for x in seats]

    m = int(input())
    groups = []
    for _ in range(m):
        g = input().split()
        groups.append([int(g[0]), g[1], g[2]])

    return n, seats, m, groups


def find_and_print_seats(group, seats):
    if group[0] == 3:
        if group[1] == "left":
            i, j = 0, 3
        else:
            i, j = 4, 7
    elif group[0] == 2:
        if group[1] == "left":
            if group[2] == "aisle":
                i, j = 1, 3
            else:
                i, j = 0, 2
        else:
            if group[2] == "aisle":
                i, j = 4, 6
            else:
                i, j = 5, 7
    elif group[0] == 1:
        if group[1] == "left":
            if group[2] == "aisle":
                i, j = 2, 3
            else:
                i, j = 0, 1
        else:
            if group[2] == "aisle":
                i, j = 4, 5
            else:
                i, j = 6, 7
    else:
        print("error")

    is_found = False
    for s in range(len(seats)):
        if seats[s][i:j] == ["." for _ in range(i, j)]:
            message = "Passengers can take seats:"
            for k in range(i, j):
                message += f" {s+1}{SEATS_DICT[k]}"
                seats[s][k] = "X"
            is_found = True
            S, I, J = s, i, j
            break

    if not is_found:
        print("Cannot fulfill passengers requirements")
    else:
        print(message)

        for seat in seats:
            print("".join(seat))

        for k in range(I, J):
            message += f" {S+1}{SEATS_DICT[k]}"
            seats[S][k] = "#"

    return seats


def main():
    n, seats, m, groups = read_input()

    for group in groups:
        seats = find_and_print_seats(group, seats)


if __name__ == "__main__":
    main()
