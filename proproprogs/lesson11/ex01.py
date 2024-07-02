# NumPy - Произведение матриц и векторов, элементы линейной алгебры
import numpy as np


def separator(sep='-'):
    print(sep * 70)


def array_info(name, arr):
    print(
        f"массив {name}:",
        type(arr),
        id(arr),
        arr.shape
    )


def main():
    # Пришло время познакомиться с одной из фундаментальных возможностей
    # пакета NumPy–матричных и векторных вычислений.
    #
    # На одном из прошлых занятий мы с вами уже видели,
    # как можно поэлементно умножать один вектор на другой
    # или одну матрицу на другую:
    a = np.arange(1, 10).reshape(3, 3)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 2140672326704 (3, 3)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    separator()

    b = np.arange(10, 19).reshape(3, 3)
    array_info('b', b)
    # массив b: <class 'numpy.ndarray'> 2140809993680 (3, 3)
    # [[10 11 12]
    #  [13 14 15]
    #  [16 17 18]]
    print(b)

    separator()

    res1 = a * b
    array_info('res1', res1)
    print(res1)
    # массив res1: <class 'numpy.ndarray'> 2409662783504 (3, 3)
    # [[ 10  22  36]
    #  [ 52  70  90]
    #  [112 136 162]]

    separator()


if __name__ == '__main__':
    main()
