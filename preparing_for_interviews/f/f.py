DIFFER = abs(ord("a") - ord("A"))


def differ_in_case(ch1: str, ch2: str) -> bool:
    return abs(ord(ch2) - ord(ch1)) == DIFFER


def convert_to_good_string(string: str) -> str:
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        elif differ_in_case(char, stack[-1]):
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


def main():
    probably_bad_string = input()
    print(convert_to_good_string(probably_bad_string))


def test():
    assert differ_in_case("A", "a") == True
    assert differ_in_case("z", "Z") == True
    assert differ_in_case("A", "b") == False
    assert differ_in_case("z", "t") == False

    assert convert_to_good_string("vxOoOoVvx") == "vxx"
    assert convert_to_good_string("abBa") == "aa"
    assert convert_to_good_string("") == ""


if __name__ == "__main__":
    test()
    main()

"""
input
vxOoOoVvx
output
vxx
"""
