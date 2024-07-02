import numpy as np


def main():
    a = np.array(
        [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
    )
    print(a, type(a), a.dtype)
    print(a[0, 0])
    print(a[0, 1])
    print(a[1, 0])
    print(a[1, 1])
    print(a[2, 0])
    print(a[2, 1])

    b = np.array(
        [
            [
                [1, 2],
                [3, 4]
            ],
            [
                [5, 6],
                [7, 8]
            ],
            [
                [9, 10],
                [11, 12]
            ]
        ]
    )

    print(b, type(b), b.dtype)
    print('-' * 30)
    print(b[0])
    print('-' * 30)
    print(b[0, 0])
    print('-' * 30)
    print(b[0, 0, 0])
    print(b[0, 0, 1])
    print('-' * 30)
    print(b[1])
    print('-' * 30)
    print(b[1, 0])


if __name__ == '__main__':
    main()
