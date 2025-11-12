def get_card_count(n, k, cards) -> int:
    cur_sum = sum(cards[0:k])
    l = k - 1
    r = n - 1
    res = cur_sum
    for i in range(k - 1):
        a = cards[l]
        b = cards[r]
        cur_sum = cur_sum - a + b
        res = max(res, cur_sum)
        l -= 1
        r -= 1
    return res


def main():
    n = int(input())
    k = int(input())
    cards = list(map(int, input().split()))
    print(get_card_count(n, k, cards))


if __name__ == "__main__":
    main()
    assert get_card_count(7, 4, [1, 1, 9, 2, 2, 2, 6]) == 17
    assert get_card_count(7, 3, [5, 8, 2, 1, 3, 4, 11]) == 24
    assert get_card_count(5, 5, [1, 2, 3, 4, 5]) == 15
"""
input
7
4
1 1 9 2 2 2 6
output
17
"""
