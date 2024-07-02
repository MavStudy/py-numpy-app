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
    # Продолжаем знакомство с операциями над массивами и посмотрим как они
    # ведут себя с булевыми операциями. Предположим, имеется одномерный массив:
    a = np.array([1, 2, 3, 10, 20, 30])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 39301840 (6,)
    # [ 1  2  3 10 20 30]
    separator()

    # добавим еще один массив:
    b = np.array([1, 2, 3, 4, 5, 6])
    array_info('b', b)
    print(b)
    separator()

    # Но использовать результат сравнения в условных операторах нельзя.
    # Следующая строчка приведет к ошибке:
    # ------------------------------------------------------------------------
    # if a == b:
    #     print("a == b")
    # ------------------------------------------------------------------------
    # if a == b:
    # ValueError: The truth value of an array with more than one element is
    # ambiguous. Use a.any() or a.all()

    # Для такого сравнения массивов необходимо получать только одно значение
    # True или False, а не объект array. Для этого в пакете NumPy существуют
    # специальная функция np.array_equal(), которую можно применить так:
    if np.array_equal(a, b):  # Это условие сработает, если оба массива a и b
        # содержат одинаковые значения элементов и равны по длине.
        print("a == b")
    else:
        print("a != b")
    separator()

    # Если нам нужно определить, что хотя бы один элемент массива удовлетворяет
    # указанному условию, то можно воспользоваться функцией any(), например:
    print(np.any(a > 5))  # True
    print(np.any(a == 5))  # False
    print(np.any(a == b))  # True
    separator()

    # Если же нужно узнать, все ли элемента массива удовлетворяют условию,
    # то используется функция all():
    print(np.all(a > 5))  # False
    print(np.all(a > 0))  # True
    print(np.all(a == b))  # False
    separator()

if __name__ == '__main__':
    main()
