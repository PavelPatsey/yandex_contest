from collections import defaultdict


def read_input():
    n = int(input())
    data = []
    for _ in range(n):
        line = input().strip().split()
        time_d_h_m = int(line[0]), int(line[1]), int(line[2])
        time_minutes = time_d_h_m[0] * 24 * 60 + time_d_h_m[1] * 60 + time_d_h_m[2]
        # data.append([time_minutes,time_d_h_m, int(line[3]), line[4]])
        data.append([time_minutes, int(line[3]), line[4]])
    return n, data


def get_travel_times(data):
    travel_times = defaultdict(int)
    id_storage = defaultdict(int)
    for record in data:
        time, id, status = record[0], record[1], record[2]
        if status == "A":
            id_storage[id] = time
        elif status == "B":
            pass
        elif status in ("C", "S"):
            dt = time - id_storage[id]
            travel_times[id] += dt
            id_storage[id] = 0

    return travel_times


def main():
    n, data = read_input()
    travel_times = get_travel_times(sorted(data, key=lambda data: data[0]))

    keys_values = [(k, v) for k, v in travel_times.items()]
    keys_values.sort(key=lambda keys_values: keys_values[0])
    values = [x[1] for x in keys_values]
    print(" ".join(str(n) for n in values))


if __name__ == "__main__":
    main()

"""
Ввод
8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B

Вывод
156 142

"""
