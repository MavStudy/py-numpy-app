# ex05.py - полезные функции по созданию матриц
import numpy as np


def main():
    a = np.mat('1 2 3 4')  # создаёт матрицу 1х4 из строки
    print(a, a.dtype)
    # [[1 2 3 4]] int32

    b = np.mat('1, 2, 3, 4')  # то же самое: создаёт матрицу 1х4 из строки
    print(b, b.dtype)

    c = np.mat('1 2; 3 4')  # возвращает матрицу 2х2
    print(c, c.dtype)
    # [[1 2]
    #  [3 4]] int32


if __name__ == '__main__':
    main()
