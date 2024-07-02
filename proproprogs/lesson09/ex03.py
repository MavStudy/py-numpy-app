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
    # Значения -inf, inf и nan
    # Предположим, имеется массив:
    a = np.array([(1, 2), (3, 4), (5, 6)])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 5550800 (3, 2)
    # [[1 2]
    #  [3 4]
    #  [5 6]]
    separator()

    # Пакет NumPy реализован максимально дружественным способом и там, где
    # можно избежать ошибок и продолжить вычисления, он это делает. Например,
    # давайте разделим все значения массива a на 0. Из математики мы знаем,
    # что на 0 делить нельзя, но, тем не менее, критической ошибки не
    # возникнет, а все элементы примут значение inf:
    print(a/0)
    # [[inf inf]
    #  [inf inf]
    #  [inf inf]]
    # ex03.py:36: RuntimeWarning: divide by zero encountered in divide print(a/0)

    # Здесь NumPy нас лишь предупредил, что встретилось деление на ноль, но
    # расчеты были завершены и все элементы равны inf.

    # Что это за значение inf? Это сокращение от английского слова
    # infinity – бесконечность. Действительно, при делении на 0 получаем
    # бесконечность. Именно это и указано в значениях элементов массива.
    # Благодаря использованию этого специального значения, NumPy избежал
    # ошибки деления на 0. Причем, inf – это полноценный элемент массивов.
    # Его можно непосредственно задать при определении:
    b = np.array(([1, 2, np.inf]))
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 42097712 (3,)
    # [ 1.  2. inf]
    separator()

    # И, далее, он может участвовать в вычислениях. Например, умножим b на ноль
    # и посмотрим, что получится:
    result = b * 0
    array_info('result', result)
    print(result)
    # массив result: <class 'numpy.ndarray'> 161766064 (3,)
    # [ 0.  0. nan]

    # Последний элемент превратился в nan.
    # Это еще одно сокращение от английского:
    #                       not a number (не число)
    separator()

    # То есть, значение nan указывает, что в результате арифметической операции
    # третий элемент перестал быть каким-либо числовым значением. Причем, это
    # определение оказывается «прилипчивым». Например, сложим все элементы
    # массива:
    c = b * 0
    array_info('c', c)
    print(c)
    # массив c: <class 'numpy.ndarray'> 161831408 (3,)
    # [ 0.  0. nan]
    separator()

    c = c.sum()  # nan
    array_info('c', c)
    print(c)
    # массив c: <class 'numpy.float64'> 51712656 ()
    # nan
    separator()

    # То есть, любые арифметические операции с nan приводят к nan.


if __name__ == '__main__':
    main()
