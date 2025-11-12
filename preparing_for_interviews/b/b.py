def get_card_count(n, k, cards) -> int:
    prefix_1 = []
    total = 0
    for x in cards[0:k]:
        total += x
        prefix_1.append(total)
    prefix_2 = []
    total = 0
    for x in list(reversed(cards))[0:k]:
        total += x
        prefix_2.append(total)
    res = -float("inf")
    for i in range(k):
        res = max(res, prefix_1[i] + prefix_2[k - 1 - i])
    return res


def main():
    n = int(input())
    k = int(input())
    cards = list(map(int, input().split()))
    print(get_card_count(n, k, cards))


if __name__ == "__main__":
    # main()
    assert get_card_count(7, 4, [1, 1, 9, 2, 2, 2, 6])
"""
input
7
4
1 1 9 2 2 2 6
output
17
"""
