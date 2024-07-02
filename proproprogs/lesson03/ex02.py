import numpy as np


def main():
    a = np.empty(10)  # создание одномерного массива с произвольными числами
    print(a, a.dtype)

    b = np.empty(10, dtype='int16')
    print(b, b.dtype)

    c = np.empty((3, 2), dtype='float32')  # возвращает матрицу 3х2 с типом
    # float32
    print(c, c.dtype)


if __name__ == '__main__':
    main()
