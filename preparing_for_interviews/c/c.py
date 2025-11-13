from collections import Counter


def get_number_of_good_pairs(numbers) -> int:
    remainders = [x % 200 for x in numbers]
    counter = Counter(remainders)
    return sum(int(n * (n - 1) / 2) for n in counter.values())


def main():
    _n = int(input())
    numbers = list(map(int, input().split()))
    print(get_number_of_good_pairs(numbers))


def test():
    assert get_number_of_good_pairs([203, 404, 204, 200, 403]) == 2
    assert get_number_of_good_pairs([1000000]) == 0
    assert get_number_of_good_pairs([2022, 2020, 2021]) == 0


if __name__ == "__main__":
    test()
    main()


"""
input
5
203 404 204 200 403
output
2
"""
