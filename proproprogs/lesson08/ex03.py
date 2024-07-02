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
    # Пусть у нас задан тот же одномерный массив:
    a = np.array([1, 2, 3])
    array_info('a', a)
    print(a)
    # массив a: <class 'numpy.ndarray'> 30912848 (3,)
    # [1 2 3]

    # Давайте теперь добавим еще один массив:
    b = np.array([3, 4, 5])
    array_info('b', b)
    print(b)
    # массив b: <class 'numpy.ndarray'> 42097712 (3,)
    # [3 4 5]

    separator()

    # и посмотрим на эти же операции, но с участием двух массивов:
    c1 = a - b  # array([-2, -2, -2])
    array_info('c1', c1)
    print(c1)
    # массив c1: <class 'numpy.ndarray'> 161769872 (3,)
    # [-2 -2 -2]

    separator()

    c2 = b + a  # array([4, 6, 8])
    array_info('c2', c2)
    print(c2)
    # массив c2: <class 'numpy.ndarray'> 161765968 (3,)
    # [4 6 8]

    separator()

    c3 = a * b  # array([3, 8, 15])
    array_info('c3', c3)
    print(c3)
    # массив c3: <class 'numpy.ndarray'> 161766064 (3,)
    # [ 3  8 15]

    separator()

    c4 = b / a  # array([3. , 2., 1.66666667])
    array_info('c4', c4)
    print(c4)
    # массив c4: <class 'numpy.ndarray'> 161770544 (3,)
    # [3.         2.         1.66666667]

    separator()

    c5 = b // a  # array([3, 2, 1], dtype=int32)
    array_info('c5', c5)
    print(c5.dtype)  # int32
    print(c5)

    separator()

    c6 = b ** a  # array([  3,  16, 125], dtype=int32)
    array_info('c6', c6)
    print(c6.dtype)
    print(c6)
    # массив c6: <class 'numpy.ndarray'> 161770352 (3,)
    # int32
    # [  3  16 125]

    separator()

    c7 = b % a  # array([0, 0, 2], dtype=int32)
    array_info('c7', c7)
    print(c7.dtype)
    print(c7)
    # массив c7: <class 'numpy.ndarray'> 161770448 (3,)
    # int32
    # [0 0 2]

    separator()

    # Везде мы видим поэлементные операции. Соответственно, чтобы они
    # выполнялись, массивы должны быть согласованы по длине. Например, если
    # взять массив:
    # b = np.array([3, 4, 5, 6])
    # и выполнить операцию
    # a + b  # ошибка: длины массивов не совпадают
    # то возникнет ошибка из-за несовпадения длин массивов.

    # Но вот такая операция с двумерным массивом b сработает:
    b = np.arange(1, 7)
    b.resize(2, 3)
    c8 = a + b
    array_info('c8', c8)
    print(c8)
    # массив c8: <class 'numpy.ndarray'> 41901104 (2, 3)
    # [[2 4 6]
    #  [5 7 9]]


if __name__ == '__main__':
    main()
