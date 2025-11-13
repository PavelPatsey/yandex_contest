def convert_to_good_string(probably_bad_string: str) -> str:
    # your code goes here
    return ""


def main():
    probably_bad_string = input()
    print(convert_to_good_string(probably_bad_string))


def test():
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
