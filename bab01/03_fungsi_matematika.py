"""Bab 1 - Representasi fungsi matematika menggunakan Python."""


def f(x):
    return x**3 - x - 2


def main():
    x = 2.0
    hasil = f(x)

    print("x =", x)
    print("f(x) =", hasil)


if __name__ == "__main__":
    main()
