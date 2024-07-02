import numpy as np


def main():
    # Функции ones, zeros, full работают по аналогии с функцией empty
    a = np.zeros((2, 3, 4))  # нелевая матрица размерностью 2x3x4
    print(a, a.dtype)

    b = np.ones([4, 3], dtype='int8')  # матрица 4х3 из единиц и типом int8
    print(b, b.dtype)

    c = np.full((3, 2), -1)  # матрица 3х2, состоящая из -1
    print(c, c.dtype)


if __name__ == '__main__':
    main()
