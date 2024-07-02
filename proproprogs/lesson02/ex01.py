# lesson02 - NumPy. Основные типы данных. Создание массивово функцией array()
import numpy as np


def main():
    a1 = np.array([1, 2, 3, 4])
    print(a1, a1.dtype)
    # [1 2 3 4] int32

    a2 = np.array([1, 2, 3, 4], 'float64')
    print(a2, a2.dtype)
    # [1. 2. 3. 4.] float64

    # print(np.sctypeDict)

    a3 = np.array([1, 2, 3, 4], 'uintc')
    print(a3, a3.dtype)
    # [1 2 3 4] uint32

    a4 = np.array([1, 2, 3, 4], 'str_')
    print(a4, a4.dtype)
    # ['1' '2' '3' '4'] <U1

    b = np.complex64(10)
    print(b, type(b))

    c = np.int16(10.5)
    print(c, type(c))
    # 10 <class 'numpy.int16'>


if __name__ == '__main__':
    main()
