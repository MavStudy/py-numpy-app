import numpy as np


def main():
    a1 = np.array([1, 2, 3, 4])
    print(type(a1), a1, a1.dtype)
    # <class 'numpy.ndarray'> [1 2 3 4] int32

    a2 = np.array([1, 2, "3", True])
    print(type(a2), a2, a2.dtype)
    # <class 'numpy.ndarray'> ['1' '2' '3' 'True'] <U11

    # первый элемент массива a2
    print(a2[0], type(a2[0]))
    # 1 <class 'numpy.str_'>

    # второй элемент массива a2
    print(a2[1], type(a2[0]))
    # 2 <class 'numpy.str_'>

    a2[1] = '123'
    print(a2[1], type(a2[0]))
    # 123 <class 'numpy.str_'>p

    print(type(a2), a2, a2.dtype)
    # <class 'numpy.ndarray'> ['1' '123' '3' 'True'] <U11

    a2[1] = 234  # Ошибки не будет, а значение автоматически будет
    # преобразовано в строку
    print(type(a2), a2, a2.dtype)
    # <class 'numpy.ndarray'> ['1' '234' '3' 'True'] <U11


if __name__ == '__main__':
    main()
