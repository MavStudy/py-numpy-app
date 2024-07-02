# ex01-02.py - Подключение NumPy
import numpy as np


# Основным объектом NumPy является массив элементов
# (ndarray), как правило, чисел
def main():
    a1 = np.array([1, 2, 3])  # from list/tuple/range
    print(type(a1), a1)  # numpy.ndarray => [1 2 3]

    a2 = a1.tolist()  # convert array  to list
    print(type(a2), a2)  # => [1, 2, 3]

    a3 = np.array([range(1, 5), range(5, 9)])  # 2D - array
    print(type(a3), a3)  # => [[1 2 3 4] [5 6 7 8]]


if __name__ == '__main__':
    main()
