def get_card_count(n, k, cards) -> int:
    def _get_card_count(l: int, r: int, step: int, acc: int):
        if step >= k:
            return acc
        a = _get_card_count(l + 1, r, step + 1, acc + cards[l])
        b = _get_card_count(l, r - 1, step + 1, acc + cards[r])
        return max(a, b)

    return _get_card_count(0, len(cards) - 1, 0, 0)


def main():
    n = int(input())
    k = int(input())
    cards = list(map(int, input().split()))
    print(get_card_count(n, k, cards))


if __name__ == "__main__":
    main()
    assert get_card_count(7, 4, [1, 1, 9, 2, 2, 2, 6])
"""
input
7
4
1 1 9 2 2 2 6
output
17
"""
