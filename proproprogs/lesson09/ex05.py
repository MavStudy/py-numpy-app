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
    # Дополнительные функции: isfinite, iscomplex, isrea
    #
    # Часто, при работе с массивами требуется определить: являются ли его
    # элементы конечными числами. Для этого используется еще одна
    # функция – isfinite():
    # Пусть имеется массив:
    b = np.array([1, 2, np.nan, np.inf, -np.inf])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 41935088 (5,)
    # [  1.   2.  nan  inf -inf]
    separator()

    result1 = np.isfinite(b)
    array_info('result1', result1)
    print(result1)
    # массив result: <class 'numpy.ndarray'> 41901104 (5,)
    # [ True  True False False False]

    # Соответственно, все не числовые элементы помечены как False,
    # а числовые – как True.
    separator()

    # Далее, мы можем уточнять тип числа: комплексное или действительное,
    # с помощью функций iscompex() и isreal(). Например:
    a = np.array([1 + 2j, 3 - 4j, 5])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 43127984 (3,)
    # [1.+2.j 3.-4.j 5.+0.j]
    result2 = np.iscomplex(a)
    array_info('result2', result2)
    print(result2)
    # массив result2: <class 'numpy.ndarray'> 161766064 (3,)
    # [ True  True False]

    # Обратите внимание, несмотря на то, что тип данных у всех элементов
    # массива complex128 (посмотреть можно через a.dtype), последний элемент
    # функция iscomplex() пометила как False, так как мнимая часть равна нулю.
    separator()

    # Аналогично работает функция isreal():
    result3 = np.isreal(a)
    array_info('result3', result3)
    print(result3)
    # массив result3: <class 'numpy.ndarray'> 161766256 (3,)
    # [False False  True]

    # Только теперь True помечены действительные числа,
    # а False – все остальные.
    separator()

    # Но, применяя эту функцию к массиву b:
    result4 = np.isreal(b)
    array_info('result4', result4)
    print(result4)
    # массив result4: <class 'numpy.ndarray'> 161770352 (5,)
    # [ True  True  True  True  True]

    # получим все значения True. То есть, специальные значения
    # nan и inf отмечаются как действительные.
    separator()


if __name__ == '__main__':
    main()
