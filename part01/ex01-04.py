# ex01-04.py - Размерность массива
import numpy as np


# Основным объектом NumPy является массив элементов
# (ndarray), как правило, чисел
def main():
    # zero-dimensional arrays
    a1 = np.array(5)  # scalar
    # a1.ndim  # 0
    print(type(a1), a1)
    print(f"a1.ndim {a1.ndim}")  # Return the number of dimensions in array
    # <class 'numpy.ndarray'> 5
    # a1.ndim 0

    # one-dimensional arrays
    a2 = np.array([1, 2, 3])  # vector
    print(type(a2), a2)
    print(f"a2.ndim {a2.ndim}")  # Return the number of dimensions in array
    # <class 'numpy.ndarray'> [1 2 3]
    # a2.ndim 1

    # multi-dimensional arrays
    a3 = np.array([[1, 2, 3], [4, 5, 6]])  # matrix
    print(type(a3), a3)
    print(f"a3.ndim {a3.ndim}")  # Return the number of dimensions in array
    # <class 'numpy.ndarray'> [[1 2 3]
    #  [4 5 6]]
    # a3.ndim 2

    a4 = np.array([
        [[111, 112], [121, 122]],
        [[211, 212], [221, 222]],
        [[311, 312], [321, 322]]
    ])
    print(type(a4), a4)
    print(f"a4.ndim {a4.ndim}")  # Return the number of dimensions in array
    # <class 'numpy.ndarray'> [[[111 112]
    #   [121 122]]

    #  [[211 212]
    #   [221 222]]

    #  [[311 312]
    #   [321 322]]]
    # a4.ndim 3


if __name__ == '__main__':
    main()
