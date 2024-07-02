import numpy as np


def main():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(a)
    b = a.reshape(3, 3)
    print(b)
    print(b[1][2])


if __name__ == '__main__':
    main()
