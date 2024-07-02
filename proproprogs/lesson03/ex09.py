# Функции формирования числовых диапазонов
import numpy as np


def main():
    # Функция arrange довольно часто применяется в программах на Python.
    # Она позволяет проходить заданный интервал с указанным шагом.
    a1 = np.arange(5)  # интервал [0; 5) с шагом 1
    print(a1, a1.dtype)
    # [0 1 2 3 4] int32

    a2 = np.arange(1, 5)   # интервал [1; 5) с шагом 1
    print(a2, a2.dtype)
    # [1 2 3 4] int32

    a3 = np.arange(1, 5, 0.5)  # интервал [1; 5) с шагом 0,5
    print(a3, a3.dtype)
    # [1.  1.5 2.  2.5 3.  3.5 4.  4.5] float64


if __name__ == '__main__':
    main()
