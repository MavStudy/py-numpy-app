# ex01-03.py - Создание массивов
import numpy as np


def main():
    # array of complex numbers
    b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex_)
    print(type(b), b)
    # <class 'numpy.ndarray'> [[1.5+0.j 2. +0.j 3. +0.j]
    #  [4. +0.j 5. +0.j 6. +0.j]]

    a1 = np.zeros((3, 6))  # zero matrix
    print(type(a1), a1)

    # <class 'numpy.ndarray'> [[0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]]

    a2 = np.ones(10)  # ones matrix
    print(type(a2), a2)
    # <class 'numpy.ndarray'> [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

    a3 = np.eye(5)  # identity matrix
    print(type(a3), a3)
    # <class 'numpy.ndarray'> [[1. 0. 0. 0. 0.]
    #  [0. 1. 0. 0. 0.]
    #  [0. 0. 1. 0. 0.]
    #  [0. 0. 0. 1. 0.]
    #  [0. 0. 0. 0. 1.]]

    a4 = np.empty((3, 6))  # reserve memory for matrix
    print(type(a4), a4)
    # <class 'numpy.ndarray'> [[0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]]

    a5 = np.arange(10, 30, 5)  # array([10, 15, 20, 25])
    print(type(a5), a5)
    # <class 'numpy.ndarray'> [10 15 20 25]

    a6 = np.linspace(0, 1, 5)  # array([0, 0.25, 0.5, 0.75, 1])
    print(type(a6), a6)
    # <class 'numpy.ndarray'> [0.   0.25 0.5  0.75 1.  ]

    a7 = np.logspace(0, 3, 4)  # array([1, 10, 100, 1000])
    print(type(a7), a7)
    # <class 'numpy.ndarray'> [   1.   10.  100. 1000.]


if __name__ == '__main__':
    main()
