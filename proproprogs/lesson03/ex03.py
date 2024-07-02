import numpy as np


def main():
    # Для функций eye и identity размерности указываются отдельными
    # параметрами
    a = np.eye(4)  # матрица 4х4
    print(a, a.dtype)

    b = np.eye(4, 2)  # матрица 4х2
    print(b, b.dtype)

    c = np.identity(5)  # матрица 5х5
    print(c, c.dtype)


if __name__ == '__main__':
    main()
