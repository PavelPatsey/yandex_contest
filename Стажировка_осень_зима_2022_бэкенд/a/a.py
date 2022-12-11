def read_input():
    n = int(input())
    data = []
    data = [input().strip().split(",") for _ in range(n)]
    return n, data


def get_cipher(surname, name, patronymic, day, mouth, year):
    number_1 = len(set(surname + name + patronymic))
    number_2 = sum([int(x) for x in day + mouth]) * 64
    number_3 = (ord(surname[0].lower()) - ord("a") + 1) * 256

    cipher_10 = number_1 + number_2 + number_3
    cipher_hex = hex(cipher_10)
    cipher_hex = cipher_hex[2:].upper()
    cipher_hex = cipher_hex[-3:]
    cipher_hex = "0" * (len(cipher_hex) - 3) + cipher_hex

    return cipher_hex[-3:]


def main():
    n, data = read_input()
    cipher_hexs = [get_cipher(*x) for x in data]
    print(" ".join(cipher_hexs))


if __name__ == "__main__":
    assert get_cipher("Volozh", "Arcady", "Yurievich", "11", "2", "1964") == "710"
    assert get_cipher("Segalovich", "Ilya", "Valentinovich", "13", "9", "1964") == "64F"
    main()

"""
Ввод
2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964

Вывод
710 64F
"""
