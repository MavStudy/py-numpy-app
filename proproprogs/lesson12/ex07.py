# NumPy - Множества (unique) и операции над ними
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
    # Операции над множествами - Симметричная разность (XOR).
    #
    # Последняя базовая операция – это вычисление симметричной разности,
    # то есть, остаются не совпадающие значения из двух множеств:
    #
    # Симметричная_разность_XOR.png
    #
    # Реализуется это с помощью функции setxor1d(x, y)
    #

    x = np.array([0, 1, 2, 3])
    array_info('x', x)
    print(x)
    # массив x: <class 'numpy.ndarray'> 1791966633520 (4,)
    # [0 1 2 3]
    separator()
    y = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    array_info('y', y)
    print(y)
    # массив y: <class 'numpy.ndarray'> 1792108797488 (8,)
    # [1 2 3 4 5 6 7 8]
    separator()

    print(np.setxor1d(x, y))
    # [0 4 5 6 7 8]


if __name__ == '__main__':
    main()
