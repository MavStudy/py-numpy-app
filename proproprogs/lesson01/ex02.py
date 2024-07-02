import numpy as np


def main():
    a = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(a)
    # [1 2 3 4 5 6 7 8 9]

    b = a[[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    print(b)
    # [2 2 2 2 2 2 2 2 2]

    c = a[[1, 1, 1, 1, 1]]
    print(c)
    # [2 2 2 2 2]

    d = a[[True, True, False, False, False, False, True, True, True]]
    print(d)
    # [1 2 7 8 9]


if __name__ == '__main__':
    main()
