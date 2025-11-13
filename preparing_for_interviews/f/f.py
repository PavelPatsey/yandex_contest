from typing import Tuple

DIFFER = abs(ord("a") - ord("A"))


def differ_in_case(ch1: str, ch2: str) -> bool:
    return abs(ord(ch2) - ord(ch1)) == DIFFER


def make_converted_string(string: str) -> Tuple[str, bool]:
    chars = []
    i = 0
    while i < len(string):
        if i == len(string) - 1:
            chars.append(string[i])
            i += 1
        elif differ_in_case(string[i], string[i + 1]):
            i += 2
        else:
            chars.append(string[i])
            i += 1
    return "".join(chars), len(chars) != len(string)


def convert_to_good_string(string: str) -> str:
    converted = True
    new_string = string
    while converted:
        new_string, converted = make_converted_string(new_string)
    return new_string


def main():
    probably_bad_string = input()
    print(convert_to_good_string(probably_bad_string))


def test():
    assert differ_in_case("A", "a") == True
    assert differ_in_case("z", "Z") == True
    assert differ_in_case("A", "b") == False
    assert differ_in_case("z", "t") == False

    assert make_converted_string("vxOoOoVvx") == ("vxx", True)

    assert convert_to_good_string("vxOoOoVvx") == "vxx"
    assert convert_to_good_string("abBa") == "aa"


if __name__ == "__main__":
    # test()
    main()

"""
input
vxOoOoVvx
output
vxx
"""
