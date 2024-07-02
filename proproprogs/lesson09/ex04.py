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
    # Функции isnan и isinf
    #
    # Так как элементы inf и nan не относятся к числам, то для их
    # идентификации, проверки, что текущий элемент массива принимает одно из
    # этих значений, существуют функции isnan() и isinf(). Они возвращают True,
    # если элемент равен nan и inf и Flase – в противном случае. Посмотрим как
    # можно их использовать в программе. Пусть имеется массив:
    b = np.array([1, 2, np.nan, np.inf, -np.inf])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 41935088 (5,)
    # [  1.   2.  nan  inf -inf]
    separator()

    result1 = np.isinf(b)
    array_info('result1', result1)
    print(result1)
    # массив result1: <class 'numpy.ndarray'> 41901104 (5,)
    # [False False False  True  True]
    separator()
    result2 = np.isnan(b)
    array_info('result2', result2)
    print(result2)
    # массив result2: <class 'numpy.ndarray'> 42800016 (5,)
    # [False False  True False False]
    separator()

    # На выходе имеем массив с булевыми значениями и True стоит на местах inf
    # (при вызове isinf) и nan (при вызове isnan). Далее, используя этот массив
    # можно исключить нечисловые элементы из массива, например, так:
    indx = np.isinf(b)
    array_info('indx', indx)
    print(indx)
    result3 = b[~indx]
    array_info('result3', result3)
    print(result3)
    # массив result3: <class 'numpy.ndarray'> 161770448 (3,)
    # [ 1.  2. nan]

    # Здесь исключаются все элементы inf, а операция ~indx инвертирует булевы
    # значения. Аналогично можно отфильтровать значения nan.
    separator()


if __name__ == '__main__':
    main()
