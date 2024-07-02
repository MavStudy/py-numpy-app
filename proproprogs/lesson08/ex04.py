# NumPy - базовые математические операции над массивами
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
    # Два небольших примера транслирования массивов, так как думаю,
    # общий принцип здесь понятен. Пусть у нас трехмерный и двумерный массивы:
    a = np.arange(1, 19)
    a.resize(3, 3, 2)
    b = np.ones((3, 2))
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 40504368 (3, 3, 2)
    # [[[ 1  2]
    #   [ 3  4]
    #   [ 5  6]]
    #
    #  [[ 7  8]
    #   [ 9 10]
    #   [11 12]]
    #
    #  [[13 14]
    #   [15 16]
    #   [17 18]]]

    separator()

    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 41966640 (3, 2)
    # [[1. 1.]
    #  [1. 1.]
    #  [1. 1.]]

    separator()

    # С ними можно выполнять такие очевидные операции:

    c1 = a - b
    array_info('c1', c1)
    print(c1)
    # массив c1: <class 'numpy.ndarray'> 42800016 (3, 3, 2)
    # [[[ 0.  1.]
    #   [ 2.  3.]
    #   [ 4.  5.]]
    #
    #  [[ 6.  7.]
    #   [ 8.  9.]
    #   [10. 11.]]
    #
    #  [[12. 13.]
    #   [14. 15.]
    #   [16. 17.]]]

    separator()

    c2 = a * 10
    array_info('c2', c2)
    print(c2)
    # массив c2: <class 'numpy.ndarray'> 161774832 (3, 3, 2)
    # [[[ 10  20]
    #   [ 30  40]
    #   [ 50  60]]
    #
    #  [[ 70  80]
    #   [ 90 100]
    #   [110 120]]
    #
    #  [[130 140]
    #   [150 160]
    #   [170 180]]]

    separator()

    c3 = a // b
    array_info('c3', c3)
    print(c3)
    # массив c3: <class 'numpy.ndarray'> 161770448 (3, 3, 2)
    # [[[ 1.  2.]
    #   [ 3.  4.]
    #   [ 5.  6.]]
    #
    #  [[ 7.  8.]
    #   [ 9. 10.]
    #   [11. 12.]]
    #
    #  [[13. 14.]
    #   [15. 16.]
    #   [17. 18.]]]

    separator()

    # И так далее. Причем, двумерный массив b может быть применен к трехмерному
    # массиву a благодаря операции транслирования, так как их размеры
    # согласованы. На самом деле, умножение трехмерного массива на число также
    # реализуется через транслирование числа по всем элементам массива a.


if __name__ == '__main__':
    main()