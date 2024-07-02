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
    # Операции над множествами - Вычитание множеств.
    # Далее, множества можно вычитать друг из друга, причем результат будет
    # зависеть от того, какое множество из какого вычитается:
    #
    # Вычитание_множеств.png
    #
    # np.setdiff1d(x, y)
    # np.setdiff1d(y, x)
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

    print(np.setdiff1d(x, y))
    # [0]
    print(np.setdiff1d(y, x))
    # [4 5 6 7 8]


if __name__ == '__main__':
    main()
