def get_card_count(n, k, cards) -> int:
    cur_sum = sum(cards[0:k])
    res = cur_sum
    for i in range(1, k + 1):
        cur_sum = cur_sum - cards[k - i] + cards[-i]
        res = max(res, cur_sum)
    return res


def main():
    n = int(input())
    k = int(input())
    cards = list(map(int, input().split()))
    print(get_card_count(n, k, cards))


if __name__ == "__main__":
    assert get_card_count(7, 4, [1, 1, 9, 2, 2, 2, 6]) == 17
    assert get_card_count(7, 3, [5, 8, 2, 1, 3, 4, 11]) == 24
    assert get_card_count(5, 5, [1, 2, 3, 4, 5]) == 15
    main()
"""
input
7
4
1 1 9 2 2 2 6
output
17
"""
