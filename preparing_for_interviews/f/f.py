import sys

sys.setrecursionlimit(10**7)
DIFFER = abs(ord("a") - ord("A"))


def differ_in_case(ch1: str, ch2: str) -> bool:
    return abs(ord(ch2) - ord(ch1)) == DIFFER


def get_differ_index(string: str) -> int:
    for i, pair in enumerate(zip(string, string[1:])):
        if differ_in_case(pair[0], pair[1]):
            return i
    return -1


def convert_to_good_string(string: str) -> str:
    i = get_differ_index(string)
    if i == -1:
        return string
    new_string = string[:i] + string[i + 2 :]
    return convert_to_good_string(new_string)


def main():
    probably_bad_string = input()
    print(convert_to_good_string(probably_bad_string))


def test():
    assert differ_in_case("A", "a") == True
    assert differ_in_case("z", "Z") == True
    assert differ_in_case("A", "b") == False
    assert differ_in_case("z", "t") == False

    assert get_differ_index("vxOoOoVvx") == 2

    assert convert_to_good_string("vxOoOoVvx") == "vxx"
    assert convert_to_good_string("abBa") == "aa"


if __name__ == "__main__":
    test()
    main()

"""
input
vxOoOoVvx
output
vxx
"""
