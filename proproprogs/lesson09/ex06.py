# NumPy - Булевы операции и функции, значения inf и nan

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
    # Функции logical_and, logical_or, logical_not и logical_xor
    #
    # В NumPy можно выполнять стандартные булевы операции И, ИЛИ, НЕ,
    # исключающее ИЛИ, применительно к данным массивов. Например, зададим два
    # массива так, чтобы попарно элементы образовывали все возможные
    # комбинации:

    # ПРОВЕРИТЬ РЕЗУЛЬТАТЫ !!!

    X = np.array([True, False, True, False])
    Y = np.array([True, True, False, False])

    # И, затем, применим к ним логические операции:
    result1 = np.logical_and(X, Y)
    array_info('result1', result1)
    print(result1)
    # массив result1: <class 'numpy.ndarray'> 42931184 (4,)
    # [ True False False False]
    separator()

    result2 = np.logical_or(X, Y)
    array_info('result2', result2)
    print(result2)
    # массив result2: <class 'numpy.ndarray'> 161769968 (4,)
    # [ True  True  True False]
    separator()

    result3 = np.logical_not(X)
    array_info('result3', result3)
    print(result3)
    # массив result3: <class 'numpy.ndarray'> 161770160 (4,)
    # [False  True False  True]
    separator()

    result4 = np.logical_xor(X, Y)
    array_info('result4', result4)
    print(result4)
    # массив result4: <class 'numpy.ndarray'> 161770352 (4,)
    # [False  True  True False]
    separator()

    # Все те же операции можно проводить и с числовыми значениями, полагая,
    # что 0 – это False, а любое другое число – True.
    # Например, два таких массива:
    a = np.array([1, 0, 2, 0])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 161766160 (4,)
    # [1 0 2 0]
    separator()

    b = np.array([3, 4, 0, 0])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 161766256 (4,)
    # [3 4 0 0]
    separator()

    print(np.logical_and(a, b))
    print(np.logical_or(a, b))
    print(np.logical_not(a))
    print(np.logical_xor(a, b))

if __name__ == '__main__':
    main()
