def get_number_of_good_pairs(numbers) -> int:
    # your code goes here
    return 0


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
    print(get_number_of_good_pairs(numbers))


def test():
    assert get_number_of_good_pairs([203, 404, 204, 200, 403]) == 2


if __name__ == "__main__":
    main()
    test()

"""
input
5
203 404 204 200 403
output
2
"""
