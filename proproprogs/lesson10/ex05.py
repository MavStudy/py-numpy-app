# NumPy - Базовые математические функции
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
    # Функции перемешивания элементов массива
    #
    # Следующие две функции:
    # np.random.shuffle()
    # np.random.permutation()
    #
    # перемешивают случайным образом элементы массива.

    # Например, дан массив:
    a = np.arange(10)
    array_info('a', a)
    print(a)
    separator()

    # И нам требуется перетасовать эго элементы.
    # В самом простом случае это делается так:
    np.random.shuffle(a)
    array_info('a', a)
    print(a)
    separator()

    # Причем, здесь меняется сам массив a. Если вызвать
    # эту функцию еще раз:
    np.random.shuffle(a)
    array_info('a', a)
    print(a)
    separator()

    # то значения еще раз перетасуются. Но, работает она
    # только с первой осью axis0. Например, если взять двумерный массив:
    a = np.arange(1, 10).reshape(3, 3)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 2045637893872 (3, 3)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    separator()

    # и вызвать эту функцию:
    np.random.shuffle(a)
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 3090520088304 (3, 3)
    # [[1 2 3]
    #  [7 8 9]
    #  [4 5 6]]

    # то в массиве aбудут переставлены только строки.
    separator()

    # торая функция возвращает случайную последовательность чисел,
    # генерируя последовательность «на лету»:
    b = np.random.permutation(10)
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 2328856260848 (10,)
    # [3 6 7 9 0 2 8 5 4 1]


if __name__ == '__main__':
    main()
