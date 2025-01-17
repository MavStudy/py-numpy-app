import numpy as np


def main():
    a = np.diag([1, 2, 3])  # диагональная матрица 3х3
    print(a, a.dtype)
    # [[1 0 0]
    #  [0 2 0]
    #  [0 0 3]] int32

    # Но, если ей передать двумерный список, то она возвратит одномерный
    # массив из элементов, стоящих на главной диагонали:
    b = np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])  # выделение элементов
    # главной диагонали
    print(b, b.dtype)
    # [1 5 9] int32

    # Если же мы хотим сформировать диагональную матрицу из многомерных
    # списков или массивов, то следует воспользоваться функцией
    c = np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    print(c, c.dtype)
    # [[1 0 0 0 0 0 0 0 0]
    #  [0 2 0 0 0 0 0 0 0]
    #  [0 0 3 0 0 0 0 0 0]
    #  [0 0 0 4 0 0 0 0 0]
    #  [0 0 0 0 5 0 0 0 0]
    #  [0 0 0 0 0 6 0 0 0]
    #  [0 0 0 0 0 0 7 0 0]
    #  [0 0 0 0 0 0 0 8 0]
    #  [0 0 0 0 0 0 0 0 9]] int32


if __name__ == '__main__':
    main()
